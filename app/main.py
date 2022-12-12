from typing import List

from fastapi_login import LoginManager
from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi_login.exceptions import InvalidCredentialsException
from sqlalchemy.orm import Session
from sqlalchemy import update

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


SECRET = "e8da7c60fdf17dd0ae5e6e6802f6faf569de0d04c368b151"
manager = LoginManager(SECRET, '/login')



# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI()


@app.post('/login')
def login(
    data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)
):
    """
    # Login
    Crée un token de connexion. Celui-ci est inutile pour le bon fonctionnement de l'API, mais il a le mérite d'exister
    """
    email = data.username
    password = data.password

    utilisateur = crud.get_utilisateur_by_email(db, email)
    if not utilisateur:
        raise InvalidCredentialsException
    elif password != utilisateur.motdepasse:
        raise InvalidCredentialsException

    print(utilisateur)

    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token}


@app.get("/utilisateurs/", response_model=List[schemas.UtilisateurModel])
def read_utilisateurs(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    # Read Utilisateurs
    Affiche la liste de tous les **utilisateurs**
    """
    utilisateur = crud.get_utilisateurs(db, skip=skip, limit=limit)
    return utilisateur


@app.get("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel)
def read_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
    """
    # Read Utilisateur
    Affiche un utilisateur
    """
    db_user = crud.get_utilisateur(db, id_utilisateur)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return db_user

@app.post("/utilisateur/", response_model=schemas.UtilisateurModel)
def create_utilisateur(
    CreateUtilisateur: schemas.UtilisateurCreate, 
    db: Session = Depends(get_db)
):
    """
    # Create Utilisateur
    Crée un **utilisateur**
    """
    db_utilisateur = crud.get_utilisateur_by_email(db, email=CreateUtilisateur.email)
    if db_utilisateur:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_utilisateur(db, CreateUtilisateur)


@app.put("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel)
def edit_utilisateur(id_utilisateur: int, EditUtilisateur: schemas.UtilisateurEdit, db: Session = Depends(get_db)):
    """
    # Edit utilisateur
    Édite un **utilisateur**
    """
    return crud.edit_utilisateur(db, EditUtilisateur, id_utilisateur)


@app.delete("/utilisateur/{id_utilisateur}")
def del_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
    """
    # Del Utilisateur
    Supprimer un utilisateur
    """
    crud.delete_utilisateur(
        db = db,
        id_utilisateur = id_utilisateur
    )


@app.get("/publications/", response_model=List[schemas.PublicationModel])
def read_publications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    # Read Publication
    Affiche toutes les **publications**
    """
    publication = crud.get_publications(db, skip=skip, limit=limit)
    return publication


@app.get("/publication/{id_publication}", response_model=schemas.PublicationModel)
def read_publication(id_publication: int, db: Session = Depends(get_db)):
    """
    # Read Publication
    Afficher une **publication** par son id
    """
    db_publication = crud.get_publication(db, id_publication)
    if db_publication is None:
        raise HTTPException(status_code=404, detail="Publication not found")
    return db_publication


@app.delete("/publication/{id_publication}")
def del_publication(id_publication: int, db: Session = Depends(get_db)):
    """
    # Del Publication
    Supprime une publication
    """
    crud.delete_publication(
        db = db,
        id_publication = id_publication
    )

        
@app.post("/publication/{id_utilisateur}", response_model=schemas.PublicationModel)
def post_publication(
    id_utilisateur: int,
    CreatePublication: schemas.PublicationCreate,
    db: Session = Depends(get_db)
):
    """
    # Post Publication
    Crée une publication
    """
    return crud.create_publications(
        db = db, 
        CreatePublication = CreatePublication, 
        id_utilisateur = id_utilisateur
    )

@app.put("/publication/{id_publication}", response_model=schemas.PublicationEdit)
def put_publication(
    id_publication: int,
    EditPublication: schemas.PublicationEdit,
    db: Session = Depends(get_db),
):
    """
    # Put Publication
    Édite une publication
    """
    return crud.edit_publication(db = db, EditPublication = EditPublication, id_publication = id_publication)