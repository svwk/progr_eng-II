from pydantic import BaseModel


class SourceText(BaseModel):
    text: str
    precision: float
