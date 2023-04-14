from fastapi import APIRouter


from models import SourceTextLen, SourceText
##from utils import Utils

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


@api_router.post("/generate_100/")
def generate_100(source: SourceText):
    """Text generation using text user input and const (100)
    value of symbols count
    - **text**: input user text
    """
    return generator.generate_text(source.text, 100)
