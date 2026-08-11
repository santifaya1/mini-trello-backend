from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app import models, schemas, auth

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


@router.post("/registro", response_model=schemas.UsuarioRespuesta)
def registrar_usuario(datos: schemas.UsuarioCrear, db: Session = Depends(get_db)):
    usuario_existente = db.query(models.Usuario).filter(
        models.Usuario.email == datos.email
    ).first()

    if usuario_existente:
        raise HTTPException(status_code=400, detail="Ese email ya está registrado")

    nuevo_usuario = models.Usuario(
        email=datos.email,
        password_hash=auth.hashear_password(datos.password),
    )

    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    return nuevo_usuario

@router.post("/login")
def login(datos: schemas.UsuarioCrear, db: Session = Depends(get_db)):
    usuario = db.query(models.Usuario).filter(
        models.Usuario.email == datos.email
    ).first()

    if not usuario or not auth.verificar_password(datos.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Email o contraseña incorrectos")

    token = auth.crear_token({"sub": usuario.email})

    return {"access_token": token, "token_type": "bearer"}