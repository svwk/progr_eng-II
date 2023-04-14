from fastapi import APIRouter
from models import SourceTextLen
from utils import Utils


api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "Формализация текста"}


@api_router.post("/generate_len/")
def generate_len(source: SourceTextLen):
    """Text generation using user input
    - **text**: input user text
    - **text_len**: count of output symbols
    """
    generator = Utils()
    return generator.generate_text(source.text, source.text_len)