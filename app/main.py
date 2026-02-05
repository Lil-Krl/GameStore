from fastapi import FastAPI
from .database import engine
from .models import Base
from .routers import users

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Game Store API",
    version="1.0.0"
)

app.include_router(users.router)
