import pytest
from main import app
from fastapi.testclient import TestClient
from models import SourceText as st

import sys
sys.path.append('.')

client = TestClient(app)


st.text = 'Hi Linda, How is it going? ' \
            'Sorry I haven not been in touch for such a long time but I have had exams so I have been studying every free minute. ' \
            'Anyway, I love to hear all your news and I am hoping we can get together soon to catch up. ' \
            'We just moved to a bigger flat so maybe you can come and visit one weekend? How is the new job? Looking forward to hearing from you! ' \
            'Helga'

st.precision = 0.9

def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Формализация текста"}

def test_post_convert():
    req = client.post("/convert/", json={"text": st.text, "precision": st.precision})
    assert req.status_code == 200
    assert req.json() != ""