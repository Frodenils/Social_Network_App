from sqlalchemy.orm import Session
from sqlalchemy import update
from fastapi import HTTPException
from . import models, schemas


def get_utilisateur(
    db: Session, 
    utilisateur_id: int
):
    return db.query(models.Utilisateur).filter(models.Utilisateur.id_utilisateur == utilisateur_id).first()


def get_utilisateur_by_email(
    db: Session, 
    email: str
):
    return db.query(models.Utilisateur).filter(models.Utilisateur.email == email).first()


def get_utilisateurs(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
):
    return db.query(models.Utilisateur).offset(skip).limit(limit).all()


def create_utilisateur(
    db: Session, 
    CreateUtilisateur: schemas.UtilisateurCreate
):
    motdepasse = CreateUtilisateur.motdepasse + "notreallyhashed"
    db_utilisateur = models.Utilisateur(
        nom=CreateUtilisateur.nom, 
        email=CreateUtilisateur.email, 
        motdepasse=motdepasse
    )
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


def edit_utilisateur(
    db: Session,
    EditUtilisateur: schemas.UtilisateurEdit,
    id_utilisateur: int,
):
    utilisateur = get_utilisateur(db, id_utilisateur)
    if utilisateur is None :
        raise HTTPException(status_code=404, detail="Utilisateur inconnu")
    motdepasse = utilisateur.motdepasse + "notreallyhashed"
    db.execute(
        update(models.Utilisateur)
        .where(utilisateur.id_utilisateur == id_utilisateur)
        .values(
            nom=EditUtilisateur.nom, 
            email=EditUtilisateur.email, 
            motdepasse=motdepasse
        )
    )
    db.commit()
    db.refresh(utilisateur)
    return utilisateur


def delete_utilisateur(
    db = Session,
    id_utilisateur = int
):
    utilisateur = get_utilisateur(
        db = db, 
        id_utilisateur = id_utilisateur
    )
    if utilisateur is None :
        raise HTTPException(status_code=404, detail=f"L'utilisateur d'identifiant !r{id_utilisateur} n'a pas été trouvé")
    db.delete(id_utilisateur)
    db.commit()


def get_publications(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
):
    return db.query(models.Publication).offset(skip).limit(limit).all()


def get_publication(
    db: Session, 
    id_publication: int
):
    return db.query(models.Publication).filter(models.Publication.id_publication == id_publication).first()


def create_publications(
    db: Session, 
    CreatePublication: schemas.PublicationCreate, 
    id_utilisateur: int
):
    db_publication = models.Publication(
        **CreatePublication.dict(),
        id_utilisateur = id_utilisateur
    )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication

def edit_publication(
    db: Session,
    EditPublication: schemas.PublicationEdit,
    id_publication: int,
):
    publication = get_publication(db = db, id_publication = id_publication)
    if publication is None :
        raise HTTPException(status_code=404, detail=f"La publication d'identifiant !r{id_publication} n'a pas été trouvé")
    db.execute(
        update(models.Publication)
        .where(publication.id_publication == id_publication)
        .values(
            titre = EditPublication.titre,
            contenu = EditPublication.contenu,
            img = EditPublication.img,
            id_utilisateur = EditPublication.id_utilisateur
        )
    )
    db.commit()
    db.refresh(publication)
    return publication


def delete_publication(
    db = Session,
    id_publication = int
):
    publication = get_publication(
        db = db, 
        id_publication = id_publication
    )
    if publication is None :
        raise HTTPException(status_code=404, detail=f"La publication d'identifiant !r{id_publication} n'a pas été trouvée")
    db.delete(publication)
    db.commit()
