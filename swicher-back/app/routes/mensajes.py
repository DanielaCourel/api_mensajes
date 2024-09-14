from fastapi import APIRouter
from app.database.models import Player, Mensaje
from pony.orm import db_session, select

router = APIRouter()

@router.get("/traerMensajes")
async def mensajes():
    # Crear un objeto en la base de datos
    with db_session():
        mensajes = select(m for m in Mensaje)[:]
    return {"mensajes": mensajes}

@router.post("/postear")
async def publicar_mensaje(username: str, mensaje: str):
    with db_session():
        player = Player.get(username=username)
        if not player:
            player = Player(username=username)
        Mensaje(mensaje=mensaje, player=player)
    return {"mensaje": mensaje, "player": username}

@router.delete("/")
async def borrar_mensajes(id: int, username: str):
    with db_session():
        mensajes = select(m for m in Mensaje if m.id == id and m.player.username == username)[:]
        if mensajes:
            mensajes.delete()
    return {"merequetengue"}