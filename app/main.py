from app.models.schemas import TextRequest
from fastapi import FastAPI, Request, BackgroundTasks
from app.routers import calculator, names, users, birds
from app.services import file_writer

app = FastAPI()
app.include_router(calculator.router)
app.include_router(names.router)
app.include_router(users.router)
app.include_router(birds.router)

@app.middleware("http")
async def log_requests(request: Request, call_next):
    print(f"Przyszło żądanie: {request.method} {request.url}")
    response = await call_next(request)
    print(f"Status odpowiedzi: {response.status_code}")
    return response

@app.post("/addtotext")
def addToText(payload: TextRequest, background_tasks: BackgroundTasks):
    background_tasks.add_task(file_writer.add_to_file, payload.text)
    return {"zapisano": payload.text}