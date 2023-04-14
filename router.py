from transformers import pipeline
from fastapi import APIRouter
from models import SourceTextLen, SourceText


api_router = APIRouter()
generator = pipeline("text-generation", "gpt2")


@api_router.get("/")
async def root():
    return {"message": "Формализация текста"}


@api_router.post("/generate_len/")
def generate_len(source: SourceTextLen):
    """Text generation using user input
    - **text**: input user text
    - **text_len**: count of output symbols
    """
    return generator.generate_text(source.text, source.text_len)