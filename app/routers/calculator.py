from fastapi import APIRouter
from app.models.schemas import AddRequest
from app.services import calculator

router = APIRouter()

@router.post("/dodaj")
def dodaj(payload: AddRequest):
    wynik = calculator.add(payload.pierwszy, payload.drugi)
    return {"wynik" : wynik}