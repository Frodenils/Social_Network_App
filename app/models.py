from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy_imageattach.entity import Image, image_attachment

from sqlalchemy.orm import relationship

from .database import Base


class Utilisateur(Base):
    __tablename__ = "Utilisateur"

    id_utilisateur = Column(Integer, primary_key=True, index=True)
    nom = Column(String)
    email = Column(String, unique=True, index=True)
    motdepasse = Column(String)

    publications = relationship("Publication", back_populates="utilisateur")


class Publication(Base):
    __tablename__ = "Publication"

    id_publication = Column(Integer, primary_key=True, index=True)
    titre = Column(String, index=True)
    contenu = Column(String, index=True)
    img = Column(String)
    # img = Column(image_attachment(""))
    id_utilisateur = Column(Integer, ForeignKey("Utilisateur.id_utilisateur"))

    utilisateur = relationship("Utilisateur", back_populates="publications")
