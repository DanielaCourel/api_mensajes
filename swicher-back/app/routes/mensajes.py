from fastapi import APIRouter
from app.database.models import Player, Mensaje
from pony.orm import db_session, select, commit
from app.schemas.mensajes import MensajeOut, MensajeIn, MensajeDelete

router = APIRouter()

@router.get("/traerMensajes", response_model=list[MensajeOut])
async def mensajes():
    with db_session():
        mensajes = select(m for m in Mensaje)[:]
        mensajes = [MensajeOut(id=m.id, mensaje=m.mensaje, player=m.player.username, id_player=m.player.id) for m in mensajes]
    return mensajes

@router.post("/postear", response_model=MensajeOut)
async def publicar_mensaje(mensaje_in: MensajeIn):
    with db_session():
        player = select(p for p in Player if p.username == mensaje_in.username).first()
        if not player:
            player = Player(username=mensaje_in.username)
        mensaje = Mensaje(mensaje=mensaje_in.mensaje, player=player)
    return MensajeOut(id=mensaje.id, mensaje=mensaje.mensaje, player=player.username, id_player=player.id)

@router.delete("/eliminarMensaje")
async def borrar_mensajes(mensaje_delete: MensajeDelete):
    with db_session():
        player = select(p for p in Player if p.username == mensaje_delete.username).first()
        if player:
            mensajes = select(m for m in Mensaje if m.id == mensaje_delete.id and m.player == player)[:]
            for mensaje in mensajes:
                mensaje.delete()
                commit()
                return {"mensaje": "Mensaje eliminado"}
            return {"mensaje": "Mensaje no encontrado"}
    return {"error": "Jugador no encontrado"}