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


@app.post("/utilisateur/", response_model=schemas.UtilisateurModel)
def create_utilisateur(utilisateur: schemas.UtilisateurCreate, db: Session = Depends(get_db)):
    db_user = crud.get_utilisateur_by_email(db, email=utilisateur.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_utilisateur(db=db, utilisateur=utilisateur)


@app.get("/utilisateur/", response_model=List[schemas.UtilisateurModel])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    utilisateur = crud.get_users(db, skip=skip, limit=limit)
    return utilisateur


@app.get("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel)
def read_user(id_utilisateur: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, id_utilisateur=id_utilisateur)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return db_user


@app.put("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel)
def edit_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
    db_utilisateur = crud.get_utilisateur(db, id_utilisateur=id_utilisateur)
    if db_utilisateur is None :
        raise HTTPException(status_code=404, detail="Utilisateur inconnu")
    return db_utilisateur



@app.post("/utilisateur/{id_utilisateur}/publications/", response_model=schemas.PublicationModel)
def create_publication_for_utilisateur(
    id_utilisateur: int, Publication: schemas.PublicationCreate, db: Session = Depends(get_db)
):
    return crud.create_utilisateur(db=db, Publication=Publication, id_utilisateur=id_utilisateur)


@app.get("/publications/", response_model=List[schemas.PublicationModel])
def read_publications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    publications = crud.get_publications(db, skip=skip, limit=limit)
    return publications
