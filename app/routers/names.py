from fastapi import APIRouter
from app.models.schemas import NameRequest
from app.services import namechecker

router = APIRouter()

@router.post("/checkname")
def checkname(payload: NameRequest):
    wynik = namechecker.checkname(payload.imie)
    return {"czy jest?:" : wynik}
