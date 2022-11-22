from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.Utilisateur)
def create_user(user: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.Utilisateur])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=schemas.Utilisateur)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return db_user


@app.post("/users/{user_id}/Publications/", response_model=schemas.Publication)
def create_Publication_for_user(
    user_id: int, Publication: schemas.PublicationCreate, db: Session = Depends(get_db)
):
    return crud.create_user_Publication(db=db, Publication=Publication, user_id=user_id)


@app.get("/Publications/", response_model=List[schemas.Publication])
def read_Publications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    Publications = crud.get_Publications(db, skip=skip, limit=limit)
    return Publications
