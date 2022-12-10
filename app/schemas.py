from typing import List, Union

from pydantic import BaseModel, Field

from . import models


class PublicationModel(BaseModel):
    id_publication: int = Field(ge=1, description="L'identifiant de la publication",example=1)
    titre: str = Field(strip_whitespace=True, description="Titre de la publication",example="La météo en charente maritime")
    contenu: str = Field(strip_whitespace=True, description="Contenu de la publication",example="Lorem Ipsum dolor sit amet")
    img: str = Field(strip_whitespace=True, description="Une image lié à la publication")
    id_utilisateur: int = Field(ge=1, description="L'identifiant de l'utilisateur lié à la publication", example=1)

class PublicationCreate(BaseModel):
    titre: str = Field(strip_whitespace=True, description="Titre de la publication",example="La météo en charente maritime")
    contenu: str = Field(strip_whitespace=True, description="Contenu de la publication",example="Lorem Ipsum dolor sit amet")
    img: str = Field(strip_whitespace=True, description="Une image lié à la publication")
    id_utilisateur: int = Field(ge=1, description="L'identifiant de l'utilisateur lié à la publication", example=1)


class UtilisateurModel(BaseModel):
    id_utilisateur: int = Field(ge=1, description="L'identifiant de l'utilisateur",example=1)
    nom: str = Field(strip_whitespace=True, description="Nom de l'utilisateur",example="Patrique Timsit")
    email: str = Field(strip_whitespace=True, description="Email de l'utilisateur",example="ptimsit@yahoo.fr")
    motdepasse: str = Field(strip_whitespace=True, description="Email de l'utilisateur",example="ptforever1234")
    publications: List[PublicationModel] = []

    class Config:
        orm_mode = True


class UtilisateurCreate(BaseModel):
    nom: str = Field(strip_whitespace=True, description="Nom de l'utilisateur",example="Patrique Timsit")
    email: str = Field(strip_whitespace=True, description="Email de l'utilisateur",example="ptimsit@yahoo.fr")
    motdepasse: str = Field(strip_whitespace=True, description="Email de l'utilisateur",example="ptforever1234")


class UtilisateurEdit(BaseModel):
    nom: str = Field(strip_whitespace=True, description="Nom de l'utilisateur",example="Patrique Timsit")
    email: str = Field(strip_whitespace=True, description="Email de l'utilisateur",example="ptimsit@yahoo.fr")
    motdepasse: str = Field(strip_whitespace=True, description="Email de l'utilisateur",example="ptforever1234")