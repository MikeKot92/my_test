from fastapi import APIRouter


router = APIRouter(prefix="/hello", tags=["Приветствие"])


@router.get("/")
async def get_hello():
    return {"Hello": "World"}


@router.get("/ru")
async def get_hello_ru():
    return {"Привет": "Мир"}


@router.get("/es")
async def get_hello_es():
    return {"Hola": "Mundo"}


@router.get("/blr")
async def get_hello_blr():
    return {"Привет": "Мир"}