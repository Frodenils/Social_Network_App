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


def get_publications(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
):
    return db.query(models.Publication).offset(skip).limit(limit).all()

def create_publications(
    db: Session, 
    CreatePublication: schemas.PublicationCreate, 
    id_utilisateur: int
):
    db_publication = models.Publication(
        **CreatePublication.dict(),
        # titre=CreatePublication.titre,
        # contenu=CreatePublication.contenu,
        # img=CreatePublication.img, 
        id_utilisateur = id_utilisateur
    )
    db.add(db_publication)
    db.commit()
    db.refresh(db_publication)
    return db_publication


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_utilisateur_item(db: Session, item: schemas.PublicationCreate, utilisateur_id: int):
    db_item = models.Item(**item.dict(), owner_id=utilisateur_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def get_publication(db: Session, publication_id: int):
    return db.query(models.Publication).filter(models.Publication.id_publication == publication_id).first()

def get_publications(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Publication).offset(skip).limit(limit).all()
def edit_publication(
    db: Session,
    EditPublication: schemas.PublicationEdit,
    id_publication: int,
    publication
):
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
