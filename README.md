# Mini Trello - Backend

API REST para gestionar tableros de tareas, inspirada en Trello. Proyecto personal paralelo a la facultad (Ingeniería en Software, Universidad Siglo 21).

## Tecnologías
- Python
- FastAPI
- SQLAlchemy (ORM)
- [Base de datos: SQLite / PostgreSQL / la que uses]

## Funcionalidades
- Registro de usuarios
- Crear tableros
- Listar tableros
- Obtener un tablero por id

## Próximamente
- Listas dentro de cada tablero
- Tarjetas y moverlas entre listas
- Autenticación de usuarios

## Cómo ejecutarlo
1. Clonar el repositorio:
   git clone https://github.com/santifaya1/mini-trello-backend.git
2. Entrar a la carpeta:
   cd mini-trello-backend
3. Instalar dependencias:
   pip install fastapi uvicorn sqlalchemy
4. Levantar el servidor:
   uvicorn app.main:app --reload
5. Abrir la documentación automática en http://127.0.0.1:8000/docs

## Autor
Santiago Faya - www.linkedin.com/in/santiago-faya-5a6b38254
