from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def get_hello():
    return {"Hello": "World"}


@app.get("/ru")
async def get_hello_ru():
    return {"Привет": "Мир"}