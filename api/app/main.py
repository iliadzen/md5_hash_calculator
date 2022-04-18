from fastapi import FastAPI
from routers import router as api_router
from database import Base, engine

Base.metadata.create_all(bind=engine)
app = FastAPI()
app.include_router(api_router)
