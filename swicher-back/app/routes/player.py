from fastapi import APIRouter, status
from app.database.models import Player
from pony.orm import db_session
from fastapi.responses import JSONResponse


router = APIRouter()

@router.get("/crear_player")
async def crear_player(username : str):
    with db_session():
        player = Player(username=username)
    return JSONResponse(status_code=status.HTTP_201_CREATED)

@router.delete("/borrar_player")
async def borrar_player(username : str):
    with db_session():
        player = Player.get(username=username)
        if player:
            player.delete()
    return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)