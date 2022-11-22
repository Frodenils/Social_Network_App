from sqlalchemy.orm import Session

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
    utilisateur: schemas.UtilisateurCreate
):
    motdepasse = utilisateur.motdepasse + "notreallyhashed"
    db_utilisateur = models.Utilisateur(
        nom=utilisateur.nom, 
        email=utilisateur.email, 
        motdepasse=motdepasse)
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


def edit_utilisateur(
    db: Session,
    utilisateur: schemas.UtilisateurEdit
):
    motdepasse = utilisateur.motdepasse + "notreallyhased"
    db_utilisateur = models.Utilisateur(
        nom=utilisateur.nom,
        email=utilisateur.email, 
        motdepasse=motdepasse, 
        publications=utilisateur.publications)
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


def get_publications(
    db: Session, 
    skip: int = 0, 
    limit: int = 100
):
    return db.query(models.Publication).offset(skip).limit(limit).all()

def create_utilisateur_publications(
    db: Session, 
    item: schemas.PublicationCreate, 
    utilisateur_id: int
):
    db_item = models.Publication(**item.dict(), owner_id=utilisateur_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
