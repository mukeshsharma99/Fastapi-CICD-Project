from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import models
from .database import Base, engine
from .dependencies import get_db
from .schemas import UserCreate, UserUpdate, UserResponse


app = FastAPI(
    title="FastAPI Cloud-Native DevSecOps Platform",
    description="Production-ready FastAPI backend with PostgreSQL, Docker, CI/CD, AWS deployment, and DevSecOps practices.",
    version="1.0.0"
)


# Create database tables
Base.metadata.create_all(bind=engine)


# -------------------------
# ROOT
# -------------------------

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL is working"}


# -------------------------
# CREATE USER
# -------------------------

@app.post("/users", response_model=UserResponse, status_code=201)
def create_user(
    user: UserCreate,
    db: Session = Depends(get_db)
):
    # Check if email already exists
    existing_user = (
        db.query(models.User)
        .filter(models.User.email == user.email)
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    new_user = models.User(
        name=user.name,
        email=user.email,
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# -------------------------
# GET ALL USERS
# -------------------------

@app.get("/users", response_model=list[UserResponse])
def get_users(
    db: Session = Depends(get_db)
):
    return db.query(models.User).all()


# -------------------------
# GET USER BY ID
# -------------------------

@app.get("/users/{user_id}", response_model=UserResponse)
def get_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    return user


# -------------------------
# UPDATE USER
# -------------------------

@app.put("/users/{user_id}", response_model=UserResponse)
def update_user(
    user_id: int,
    user_data: UserUpdate,
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # Check whether another user already has this email
    existing_user = (
        db.query(models.User)
        .filter(
            models.User.email == user_data.email,
            models.User.id != user_id
        )
        .first()
    )

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Email already registered"
        )

    user.name = user_data.name
    user.email = user_data.email

    db.commit()
    db.refresh(user)

    return user


# -------------------------
# DELETE USER
# -------------------------

@app.delete("/users/{user_id}")
def delete_user(
    user_id: int,
    db: Session = Depends(get_db)
):
    user = (
        db.query(models.User)
        .filter(models.User.id == user_id)
        .first()
    )

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    db.delete(user)
    db.commit()

    return {"message": "User deleted successfully"}