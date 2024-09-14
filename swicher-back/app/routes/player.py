from fastapi import APIRouter, status
from app.database.models import Player
from pony.orm import db_session, select
from fastapi.responses import JSONResponse
from app.schemas.player import PlayerCreate, PlayerDelete


router = APIRouter()

@router.post("/crear_player", response_model=PlayerCreate)
async def crear_player(player: PlayerCreate):
    with db_session():
        player = Player(username=player.username)
    return JSONResponse(status_code=status.HTTP_201_CREATED, content={"message": "Player created successfully"})

@router.delete("/borrar_player")
async def borrar_player(player: PlayerDelete):
    with db_session():
        player = select(p for p in Player if p.username == player.username).first()
        if player:
            player.delete()
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Player delete successfully"})