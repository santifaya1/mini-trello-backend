from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas
from app.auth import obtener_usuario_actual

router = APIRouter(prefix="/tableros", tags=["tableros"])


@router.post("/", response_model=schemas.TableroRespuesta)
def crear_tablero(
    datos: schemas.TableroCrear,
    db: Session = Depends(get_db),
    usuario_actual: models.Usuario = Depends(obtener_usuario_actual),
):
    nuevo_tablero = models.Tablero(
        nombre=datos.nombre,
        usuario_id=usuario_actual.id,
    )
    db.add(nuevo_tablero)
    db.commit()
    db.refresh(nuevo_tablero)
    return nuevo_tablero


@router.get("/", response_model=list[schemas.TableroRespuesta])
def listar_tableros(
    db: Session = Depends(get_db),
    usuario_actual: models.Usuario = Depends(obtener_usuario_actual),
):
    tableros = db.query(models.Tablero).filter(
        models.Tablero.usuario_id == usuario_actual.id
    ).all()
    return tableros

from fastapi import HTTPException


@router.get("/{tablero_id}", response_model=schemas.TableroRespuesta)
def obtener_tablero(
    tablero_id: str,
    db: Session = Depends(get_db),
    usuario_actual: models.Usuario = Depends(obtener_usuario_actual),
):
    tablero = db.query(models.Tablero).filter(
        models.Tablero.id == tablero_id,
        models.Tablero.usuario_id == usuario_actual.id,
    ).first()

    if tablero is None:
        raise HTTPException(status_code=404, detail="Tablero no encontrado")

    return tablero