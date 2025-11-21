import uvicorn
from fastapi import FastAPI

from app.db import Base, engine
from app.routers.url_router import router as urls_router

app = FastAPI()
app.include_router(urls_router)

if __name__ == "__main__":
    Base.metadata.create_all(bind=engine)
    
    uvicorn.run(app="main:app",
                reload=True)