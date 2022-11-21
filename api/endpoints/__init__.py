from fastapi import APIRouter
router = APIRouter()


@router.get("/")
def read_root():
    return {"Social-Network-App": "HELLO"}
