from fastapi import APIRouter
from models import SourceText
from generator import Generator


api_router = APIRouter()


@api_router.get("/")
async def root():
    return {"message": "Формализация текста"}


@api_router.post("/convert/")
def generate_len(source: SourceText):
    """Convert sentence from casual style to formal
    - **text**: input user text
    - **presicion**: precision of convertation, 0 to 1, more - better, but slower
    """
    gen = Generator()
    return gen.generate_text(source.text, source.precision)
