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


<<<<<<< HEAD
@app.get("/utilisateurs/", response_model=List[schemas.UtilisateurModel])
def read_utilisateurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
=======
@app.put("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel, description="Édite un utilisateur")
def edit_utilisateur(id_utilisateur: int, EditUtilisateur: schemas.UtilisateurEdit, db: Session = Depends(get_db)):
    """
    # Edit utilisateur

    Édite un utilisateur
    """
    return crud.edit_utilisateur(db, EditUtilisateur, id_utilisateur)


@app.get("/utilisateurs/", response_model=List[schemas.UtilisateurModel], description="Affiche la liste des utilisateurs")
def read_utilisateurs(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    # Read Utilisateurs

    Affiche la liste de tous les utilisateurs
    """
>>>>>>> come
    utilisateur = crud.get_utilisateurs(db, skip=skip, limit=limit)
    return utilisateur


<<<<<<< HEAD
@app.get("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel)
def read_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
=======
@app.get("/utilisateur/{id_utilisateur}", response_model=schemas.UtilisateurModel, description="Affiche un utilisateur")
def read_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
    """
    # Get Utilisateur

    Affiche l'**utilisateur** dont l'identifiant est donné en paramètre.
    """
>>>>>>> come
    db_user = crud.get_utilisateur(db, id_utilisateur)
    if db_user is None:
        raise HTTPException(status_code=404, detail="Utilisateur not found")
    return db_user
    
@app.get("/publications/", response_model=List[schemas.PublicationModel], description="Affiche les publications")
def read_publications(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db)
):
    """
    # Read Publications


@app.get("/publications/", response_model=List[schemas.PublicationModel])
def read_Publications(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """
    # Get all publications
    Afficher toutes les publications
    """
    publication = crud.get_Publications(db, skip=skip, limit=limit)
    return publication

@app.get("/publication/{id_publication}", response_model=schemas.PublicationModel)
def read_publication(id_publication: int, db: Session = Depends(get_db)):
    """
    # Get one publication by id
    Afficher une publication par son id
    """
    db_publication = crud.get_publication(db, id_publication)
    if db_publication is None:
        raise HTTPException(status_code=404, detail="Publication not found")
    return db_publication


@app.delete("/utilisateur/{id_utilisateur}")
def read_utilisateur(id_utilisateur: int, db: Session = Depends(get_db)):
    db_utilisateur = crud.get_utilisateur(db, id_utilisateur)
    with db as session:
        if not db_utilisateur:
            raise HTTPException(status_code=404, detail="Utilisateur not found")
        session.delete(db_utilisateur)
        session.commit()
        return {"ok": True}


@app.delete("/publication/{id_publication}")
def id_publication(id_publication: int, db: Session = Depends(get_db)):
    db_publication = crud.get_publication(db, id_publication)
    with db as session:
        if not db_publication:
            raise HTTPException(status_code=404, detail="Publication not found")
        session.delete(db_publication)
        session.commit()
        return {"ok": True}
    Affiche toutes les publications
    """
    publications = crud.get_publications(db, skip, limit)
    return publications

@app.post("/publication/{id_utilisateur}", response_model=schemas.PublicationModel, description="Crée une publication")
def post_publication(
    id_utilisateur: int,
    CreatePublication: schemas.PublicationCreate,
    db: Session = Depends(get_db)
):
    """
    # Post Publication

    Crée une publication
    """
    return crud.create_utilisateur_publications(
        db = db, 
        CreatePublication = CreatePublication, 
        id_utilisateur = id_utilisateur
    )

@app.put("/publication/{id_publication}", response_model=schemas.PublicationEdit, description="Édite une publication")
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
