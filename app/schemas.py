from typing import List, Union

from pydantic import BaseModel


class PublicationBase(BaseModel):
    titre: str
    description: Union[str, None] = None


class PublicationCreate(PublicationBase):
    pass


class Publication(PublicationBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UtilisateurBase(BaseModel):
    email: str


class UtilisateurCreate(UtilisateurBase):
    password: str


class Utilisateur(UtilisateurBase):
    id_utilisateur: int
    nom: str
    mail: str
    items: List[Publication] = []

    class Config:
        orm_mode = True
