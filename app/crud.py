from sqlalchemy.orm import Session

from . import models, schemas


def get_utilisateur(db: Session, utilisateur_id: int):
    return db.query(models.utilisateur).filter(models.utilisateur.id == utilisateur_id).first()


def get_utilisateur_by_email(db: Session, email: str):
    return db.query(models.utilisateur).filter(models.utilisateur.email == email).first()


def get_utilisateurs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.utilisateur).offset(skip).limit(limit).all()


def create_utilisateur(db: Session, utilisateur: schemas.UtilisateurCreate):
    fake_hashed_password = utilisateur.password + "notreallyhashed"
    db_utilisateur = models.utilisateur(email=utilisateur.email, hashed_password=fake_hashed_password)
    db.add(db_utilisateur)
    db.commit()
    db.refresh(db_utilisateur)
    return db_utilisateur


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Item).offset(skip).limit(limit).all()


def create_utilisateur_item(db: Session, item: schemas.PublicationCreate, utilisateur_id: int):
    db_item = models.Item(**item.dict(), owner_id=utilisateur_id)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item
