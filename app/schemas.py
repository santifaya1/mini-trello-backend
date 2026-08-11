from pydantic import BaseModel, EmailStr
from datetime import datetime


class UsuarioCrear(BaseModel):
    email: EmailStr
    password: str


class UsuarioRespuesta(BaseModel):
    id: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True