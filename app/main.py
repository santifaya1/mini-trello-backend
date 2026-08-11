from fastapi import FastAPI

from app.database import engine, Base
from app import models
from app.routers import usuarios

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini Trello API")

app.include_router(usuarios.router)


@app.get("/")
def read_root():
    return {"mensaje": "Mini Trello API funcionando"}