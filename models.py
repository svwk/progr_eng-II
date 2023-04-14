from pydantic import BaseModel


class SourceTextLen(BaseModel):
    text: str
    text_len: int
