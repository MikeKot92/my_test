from fastapi import FastAPI
from api import router as hello_router

app = FastAPI()

app.include_router(hello_router)
