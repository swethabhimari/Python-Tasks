# ============================================================
# 🔐 FastAPI TODO App + JWT Authentication (Array Version)
# ============================================================

# ============================================================
# 🚀 WHAT WE ARE BUILDING
# ============================================================

'''
This project includes:

✅ FastAPI
✅ JWT Authentication
✅ CRUD Operations
✅ MySQL Database Storage
'''

# ============================================================
# 🚀 INSTALL REQUIRED PACKAGES
# ============================================================

'''
pip install fastapi uvicorn python-jose sqlalchemy pymysql
'''

# ============================================================
# 📦 IMPORTS
# ============================================================

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
from jose import JWTError, jwt
from datetime import datetime, timedelta
from typing import List

# ================= MYSQL IMPORTS (ADDED ONLY) =================

from sqlalchemy import create_engine, Column, Integer, String, Boolean
from sqlalchemy.orm import sessionmaker, declarative_base, Session

# ============================================================
# 🚀 CREATE FASTAPI APP
# ============================================================

app = FastAPI()

# ============================================================
# 🔐 JWT CONFIGURATION
# ============================================================

'''
SECRET_KEY
-----------
Used to sign the token.

Think:
JWT Token = Locked Box
SECRET_KEY = Key to lock/unlock

If secret key changes:
- Old tokens become invalid
'''

SECRET_KEY = "mysecretkey"

# ------------------------------------------------------------

'''
ALGORITHM
-----------
Encryption algorithm used to create token.

HS256 = Most commonly used JWT algorithm
'''

ALGORITHM = "HS256"

# ------------------------------------------------------------

'''
TOKEN EXPIRY TIME
------------------
Defines how long token stays valid.

CHANGED ONLY: 5 minutes → 10 minutes
'''

ACCESS_TOKEN_EXPIRE = timedelta(minutes=10)

# ============================================================
# 🗄️ MYSQL CONFIGURATION (ONLY CHANGE DB NAME)
# ============================================================

DATABASE_URL = "mysql+pymysql://root:root123@localhost/todo_database"

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()

# ============================================================
# 📋 MYSQL TABLE
# ============================================================

class TodoTable(Base):

    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    completed = Column(Boolean, default=False)

# ============================================================
# 🛠️ CREATE TABLE
# ============================================================

Base.metadata.create_all(bind=engine)

# ============================================================
# 🔄 DB SESSION
# ============================================================

def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()

# ============================================================
# 🧾 Pydantic Models
# ============================================================

class Todo(BaseModel):

    id: int
    title: str
    completed: bool = False

# ------------------------------------------------------------

class Login(BaseModel):

    username: str
    password: str

# ============================================================
# 🗃️ TEMPORARY DATABASE (REMOVED ARRAY BECAUSE MYSQL USED)
# ============================================================

# todos: List[Todo] = []   ❌ replaced by database

# ============================================================
# 🔐 CREATE JWT TOKEN
# ============================================================

def create_access_token(data: dict):

    '''
    Steps:
    1. Copy incoming data
    2. Add expiry time
    3. Encode token using secret key
    4. Return generated JWT token
    '''

    to_encode = data.copy()

    expire = datetime.utcnow() + ACCESS_TOKEN_EXPIRE

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(
        to_encode,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return encoded_jwt

# ============================================================
# 🔐 TOKEN VALIDATION
# ============================================================

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_token(token: str = Depends(oauth2_scheme)):

    '''
    This function validates token.

    Steps:
    1. Read token from request
    2. Decode token
    3. Verify secret key
    4. Verify expiry time
    5. Extract user info
    '''

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if username is None:

            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

        return username

    except JWTError:

        '''
        Happens when:
        - Token expired
        - Wrong secret key
        - Invalid token
        '''

        raise HTTPException(
            status_code=401,
            detail="Token expired or invalid"
        )

# ============================================================
# 🏠 HOME API
# ============================================================

@app.get("/")
def home():

    return {
        "message": "FastAPI + JWT + MySQL 🚀"
    }

# ============================================================
# 🔐 LOGIN API
# ============================================================

@app.post("/login")
def login(user: Login):

    '''
    Dummy Login

    Username = admin
    Password = admin123
    '''

    if user.username != "admin" or user.password != "admin123":

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
        "expires_in": "5 minutes"
    }

# ============================================================
# ✅ CREATE TODO
# ============================================================

@app.post("/todos")
def create_todo(
    todo: Todo,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    new_todo = TodoTable(
        id=todo.id,
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)

    return {
        "message": "Todo created",
        "data": new_todo
    }

# ============================================================
# ✅ READ ALL TODOS
# ============================================================

@app.get("/todos")
def get_all_todos(
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todos = db.query(TodoTable).all()

    return {
        "count": len(todos),
        "data": todos
    }

# ============================================================
# ✅ READ SINGLE TODO
# ============================================================

@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoTable).filter(TodoTable.id == todo_id).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo

# ============================================================
# ❌ DELETE TODO
# ============================================================

@app.delete("/todos/{todo_id}")
def delete_todo(
    todo_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(verify_token)
):

    todo = db.query(TodoTable).filter(TodoTable.id == todo_id).first()

    if not todo:

        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    db.delete(todo)
    db.commit()

    return {
        "message": "Todo deleted successfully"
    }