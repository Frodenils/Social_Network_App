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


@app.post("/utilisateur/", response_model=schemas.UtilisateurModel, description="Crée un utilisateur")
def create_utilisateur(
    CreateUtilisateur: schemas.UtilisateurCreate, 
    db: Session = Depends(get_db)
):
    """
    # Create Utilisateur

    Crée un utilisateur
    """
    db_utilisateur = crud.get_utilisateur_by_email(db, email=CreateUtilisateur.email)
    if db_utilisateur:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_utilisateur(db, CreateUtilisateur)


@app.put("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel, description="Édite un utilisateur")
def edit_utilisateur(id_utilisateur: int, utilisateur: schemas.UtilisateurEdit, db: Session = Depends(get_db)):
    """
    # Edit utilisateur

    Édite un utilisateur
    """
    db_utilisateur = crud.get_utilisateur(db, id_utilisateur)
    if db_utilisateur is None :
        raise HTTPException(status_code=404, detail="Utilisateur inconnu")
    return crud.edit_utilisateur(db, utilisateur, db_utilisateur, id_utilisateur)


@app.get("/utilisateurs/", response_model=List[schemas.UtilisateurModel], description="Affiche la liste des utilisateurs")
def read_utilisateurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    # Read Utilisateurs

    Affiche la liste de tous les utilisateurs
    """
    utilisateur = crud.get_utilisateurs(db, skip=skip, limit=limit)
    return utilisateur


@app.get("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel, description="Affiche un utilisateur")
def read_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
    """
    # Get Utilisateur

    Affiche l'**utilisateur** dont l'identifiant est donné en paramètre.
    """
    db_user = crud.get_utilisateur(db, id_utilisateur)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return db_user
    

@app.post("/publication/{id_utilisateur}", response_model=schemas.PublicationModel, description="Crée une publication")
def create_publication(
    id_utilisateur: int,
    CreatePublication: schemas.PublicationCreate,
    db: Session = Depends(get_db)
):
    """
    # Create Publication

    Crée une publication
    """
    return crud.create_utilisateur_publications(
        db = db, 
        CreatePublication = CreatePublication, 
        id_utilisateur = id_utilisateur
    )

@app.get("/publications/", response_model=List[schemas.PublicationModel], description="Affiche les publications")
def read_publications(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    # Read Publications

    Affiche toutes les publications
    """
    publications = crud.get_publications(db, skip, limit)
    return publications
