from pydantic import BaseModel


class ApiRequestImie(BaseModel):
    imie: str