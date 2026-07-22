from pydantic import BaseModel

class ApiRequest(BaseModel):
    pierwszy: int
    drugi: int