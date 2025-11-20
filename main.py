from fastapi import FastAPI
from app.db import Base, engine
from app.api.urls import router as urls_router

Base.metadata.create_all(bind=engine)

app = FastAPI()
app.include_router(urls_router)