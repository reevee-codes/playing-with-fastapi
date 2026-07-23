from pydantic import BaseModel

class AddRequest(BaseModel):
    pierwszy: int
    drugi: int

class NameRequest(BaseModel):
    imie: str

class TextRequest(BaseModel):
    text: str