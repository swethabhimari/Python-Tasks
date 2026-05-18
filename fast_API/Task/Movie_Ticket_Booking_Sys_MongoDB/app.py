from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
from datetime import datetime
from bson import ObjectId

# ================= MONGO DB =================

client = MongoClient("mongodb+srv://johnnyysg05_db_user:swetha1234@test.wmpbutc.mongodb.net/movie_booking_db?retryWrites=true&w=majority")
db = client["movie_booking_db"]

movies_col = db["movies"]
bookings_col = db["bookings"]

# ================= APP =================

app = FastAPI(title="Movie Booking System (MongoDB)")

# ================= MODELS =================

class MovieSchema(BaseModel):
    name: str
    genre: str
    duration: int
    show_time: str
    available_seats: int


class BookingSchema(BaseModel):
    user_name: str
    tickets: int

# ================= HELPER =================

def serialize(obj):
    obj["_id"] = str(obj["_id"])
    return obj

# ================= HOME =================

@app.get("/")
def home():
    return {"message": "Movie Booking System Running (MongoDB)"}

# ================= MOVIES =================

@app.post("/movies")
def add_movie(movie: MovieSchema):
    result = movies_col.insert_one(movie.dict())
    return {"message": "Movie Added", "id": str(result.inserted_id)}

@app.get("/movies")
def get_movies():
    movies = list(movies_col.find())
    return [serialize(m) for m in movies]

@app.get("/movies/{movie_id}")
def get_movie(movie_id: str):
    movie = movies_col.find_one({"_id": ObjectId(movie_id)})

    if not movie:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    return serialize(movie)

@app.put("/movies/{movie_id}")
def update_movie(movie_id: str, movie: MovieSchema):
    result = movies_col.update_one(
        {"_id": ObjectId(movie_id)},
        {"$set": movie.dict()}
    )

    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    return {"message": "Movie Updated"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: str):
    result = movies_col.delete_one({"_id": ObjectId(movie_id)})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    return {"message": "Movie Deleted"}

# ================= SEARCH =================

@app.get("/search-movie/{name}")
def search_movie(name: str):
    movies = movies_col.find({"name": {"$regex": name, "$options": "i"}})
    return [serialize(m) for m in movies]

# ================= BOOKING =================

@app.post("/book-ticket/{movie_id}")
def book_ticket(movie_id: str, booking: BookingSchema):

    movie = movies_col.find_one({"_id": ObjectId(movie_id)})

    if not movie:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    if movie["available_seats"] < booking.tickets:
        raise HTTPException(status_code=400, detail="Not enough seats")

    # reduce seats
    movies_col.update_one(
        {"_id": ObjectId(movie_id)},
        {"$inc": {"available_seats": -booking.tickets}}
    )

    new_booking = {
        "user_name": booking.user_name,
        "movie_id": movie_id,
        "tickets": booking.tickets,
        "booking_time": datetime.utcnow()
    }

    result = bookings_col.insert_one(new_booking)

    return {"message": "Booked Successfully", "booking_id": str(result.inserted_id)}

@app.get("/bookings")
def get_bookings():
    bookings = list(bookings_col.find())
    return [serialize(b) for b in bookings]

@app.post("/cancel-ticket/{booking_id}")
def cancel_ticket(booking_id: str):

    booking = bookings_col.find_one({"_id": ObjectId(booking_id)})

    if not booking:
        raise HTTPException(status_code=404, detail="Booking Not Found")

    movie_id = booking["movie_id"]

    # restore seats
    movies_col.update_one(
        {"_id": ObjectId(movie_id)},
        {"$inc": {"available_seats": booking["tickets"]}}
    )

    bookings_col.delete_one({"_id": ObjectId(booking_id)})

    return {"message": "Cancelled Successfully"}