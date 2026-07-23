from fastapi import APIRouter

router = APIRouter(prefix="/ptaki")

@router.get("/")
def getbirbs():
    return ["sowa", "pustułka"]

@router.post("/")
def createbird():
    #todo
    return {"status": "created"}