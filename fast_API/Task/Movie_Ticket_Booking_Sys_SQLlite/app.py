from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker, declarative_base
from datetime import datetime

# ================= DATABASE (SQLite) =================

DATABASE_URL = "sqlite:///./movie_booking.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

# ================= SCHEMAS =================

class MovieSchema(BaseModel):
    name: str
    genre: str
    duration: int
    show_time: str
    available_seats: int


class BookingSchema(BaseModel):
    user_name: str
    tickets: int

# ================= MODELS =================

class Movie(Base):
    __tablename__ = "movies"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    genre = Column(String)
    duration = Column(Integer)
    show_time = Column(String)
    available_seats = Column(Integer)


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String)
    movie_id = Column(Integer)
    tickets = Column(Integer)
    booking_time = Column(DateTime, default=datetime.utcnow)

# Create tables
Base.metadata.create_all(bind=engine)

# ================= APP =================

app = FastAPI(title="Movie Booking System (SQLite)")

# ================= HOME =================

@app.get("/")
def home():
    return {"message": "Movie Booking System Running (SQLite)"}

# ================= MOVIES =================

@app.post("/movies")
def add_movie(movie: MovieSchema):
    db = SessionLocal()
    new_movie = Movie(**movie.dict())
    db.add(new_movie)
    db.commit()
    db.refresh(new_movie)
    db.close()
    return {"message": "Movie Added"}

@app.get("/movies")
def get_movies():
    db = SessionLocal()
    data = db.query(Movie).all()
    db.close()
    return data

@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()
    db.close()

    if not movie:
        raise HTTPException(status_code=404, detail="Movie Not Found")

    return movie

@app.put("/movies/{movie_id}")
def update_movie(movie_id: int, movie_data: MovieSchema):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie Not Found")

    movie.name = movie_data.name
    movie.genre = movie_data.genre
    movie.duration = movie_data.duration
    movie.show_time = movie_data.show_time
    movie.available_seats = movie_data.available_seats

    db.commit()
    db.close()

    return {"message": "Updated"}

@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):
    db = SessionLocal()
    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie Not Found")

    db.delete(movie)
    db.commit()
    db.close()

    return {"message": "Deleted"}

# ================= SEARCH =================

@app.get("/search-movie/{name}")
def search_movie(name: str):
    db = SessionLocal()
    movies = db.query(Movie).filter(Movie.name.like(f"%{name}%")).all()
    db.close()
    return movies

# ================= BOOKING =================

@app.post("/book-ticket/{movie_id}")
def book_ticket(movie_id: int, booking: BookingSchema):
    db = SessionLocal()

    movie = db.query(Movie).filter(Movie.id == movie_id).first()

    if not movie:
        db.close()
        raise HTTPException(status_code=404, detail="Movie Not Found")

    if movie.available_seats < booking.tickets:
        db.close()
        raise HTTPException(status_code=400, detail="Not enough seats")

    movie.available_seats -= booking.tickets

    new_booking = Booking(
        user_name=booking.user_name,
        movie_id=movie_id,
        tickets=booking.tickets
    )

    db.add(new_booking)
    db.commit()
    db.refresh(new_booking)
    db.close()

    return {"message": "Booked Successfully"}

@app.post("/cancel-ticket/{booking_id}")
def cancel_ticket(booking_id: int):
    db = SessionLocal()

    booking = db.query(Booking).filter(Booking.id == booking_id).first()

    if not booking:
        db.close()
        raise HTTPException(status_code=404, detail="Booking Not Found")

    movie = db.query(Movie).filter(Movie.id == booking.movie_id).first()

    movie.available_seats += booking.tickets

    db.delete(booking)
    db.commit()
    db.close()

    return {"message": "Cancelled Successfully"}

@app.get("/bookings")
def get_bookings():
    db = SessionLocal()
    data = db.query(Booking).all()
    db.close()
    return data