import uuid
from datetime import datetime

from sqlalchemy import Column, String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship

from app.database import Base


def generar_uuid():
    return str(uuid.uuid4())


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(String, primary_key=True, default=generar_uuid)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    tableros = relationship("Tablero", back_populates="propietario")


class Tablero(Base):
    __tablename__ = "tableros"

    id = Column(String, primary_key=True, default=generar_uuid)
    usuario_id = Column(String, ForeignKey("usuarios.id"), nullable=False)
    nombre = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    propietario = relationship("Usuario", back_populates="tableros")
    tareas = relationship("Tarea", back_populates="tablero", cascade="all, delete-orphan")


class Tarea(Base):
    __tablename__ = "tareas"

    id = Column(String, primary_key=True, default=generar_uuid)
    tablero_id = Column(String, ForeignKey("tableros.id"), nullable=False)
    titulo = Column(String, nullable=False)
    estado = Column(String, default="pendiente")
    orden = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    tablero = relationship("Tablero", back_populates="tareas")