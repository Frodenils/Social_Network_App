from fastapi import Path, Depends, APIRouter, HTTPException
from pydantic import BaseModel, Field, constr
from typing import Any
from dao.daonetwork import get_utilisateur_dao

from fastapi import FastAPI


app = FastAPI()

def valid_utilisateur_from_path(
    id_utilisateur: int = Path(ge=1, description="identifiant de l'utilisateur", example=1)
) -> dict[str | Any]:
    found_utilisateur = get_utilisateur_dao(id_utilisateur)
    if found_utilisateur is None:
        raise HTTPException(
            status_code=404,
            detail=f"L'utilisateur d'id {id_utilisateur!r} n'a pas été trouvé !"
        )
    return found_utilisateur

class UtilisateurModel(BaseModel):
    id: int = Field(ge=1, description="identifiant de l'utilisateur", example=1)
    nom: constr(strip_whitespace=True, min_length=1, max_length=255) = Field(description="Nom de l'utilisateur", example="Patrick Timsit")
    mail: constr(strip_whitespace=True, min_length=1, max_length=255) = Field(description="Mail de l'utilisateur", example="p.timsit@yahoo.fr")
    mdp: constr(strip_whitespace=True, min_length=1, max_length=255) = Field(description="Mot de passe de l'utilisateur", example="ptmdp1234")


@app.get("/utilisateur/{id_utilisateur}", response_model=UtilisateurModel, summary="Afficher un utilisateur")
def get_utilisateur(
    utilisateur = Depends(valid_utilisateur_from_path)
):
    return utilisateur