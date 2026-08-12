from fastapi import FastAPI, Depends

from app.database import engine, Base
from app import models
from app.routers import usuarios, tableros
from app.auth import obtener_usuario_actual

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Trello API")

app.include_router(usuarios.router)
app.include_router(tableros.router)


@app.get("/")
def read_root():
    return {"mensaje": "Mini Trello API funcionando"}


@app.get("/perfil")
def leer_perfil(usuario_actual: models.Usuario = Depends(obtener_usuario_actual)):
    return {"email": usuario_actual.email, "id": usuario_actual.id}