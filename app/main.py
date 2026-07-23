from app.models.schemas import TextRequest, AddRequest, NameRequest
from app.services.calculator import dodawacz
from fastapi import FastAPI, APIRouter, Request, BackgroundTasks
from app.services.namechecker import namechecker
from app.services.utils import utils

app = FastAPI()

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Przyszło żądanie: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Status odpowiedzi: {response.status_code}")
    return response

@app.post("/addtotext")
def addToText(payload: TextRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(utils.addToFile(payload.text))
    return {"zapisano": payload.text}

@app.post("/dodaj")
def dodaj(payload: AddRequest):
    wynik = dodawacz.add(payload.pierwszy, payload.drugi)
    return {"wynik" : wynik}

@app.post("/checkname")
def checkname(payload: NameRequest):
    wynik =  namechecker.checkname(payload.imie)
    return {"czy jest?:" : wynik}

@app.get("/users")
def get_users():
    return ["Jan", "Anna"]

router = APIRouter(prefix="/ptaki")

@router.get("/")
def getbirbs():
    return ["sowa", "pustułka"]

@router.post("/")
def createbird():
    #todo
    return {"status": "created"}


app.include_router(router)
for route in app.routes:
    print(route.path)