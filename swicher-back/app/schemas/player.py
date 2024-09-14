from pydantic import BaseModel

class PlayerCreate(BaseModel):
    username: str

class PlayerDelete(BaseModel):
    username: str