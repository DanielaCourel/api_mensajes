"""
Los archivos de schemas se utilizan para definir los esquemas Pydantic. Siven para crear validaciones 
y manejar los datos que se envían y reciben en las peticiones HTTP.
"""

from pydantic import BaseModel

class MensajeOut(BaseModel):
    id: int
    mensaje: str
    player: str
    id_player: int

class MensajeIn(BaseModel):
    username: str
    mensaje: str

class MensajeDelete(BaseModel):
    id: int
    username: str