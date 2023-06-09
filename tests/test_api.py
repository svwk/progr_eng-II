import sys
from fastapi.testclient import TestClient

import params_t as pt
from main import app

sys.path.append('.')
client = TestClient(app)


def test_get():
    """Testing get request"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Формализация текста"}


def test_post_convert():
    """Testing post request for text generation"""
    req = client.post("/convert/", json={"text": pt.st.text, "precision": pt.st.precision})
    assert req.status_code == 200
    assert req.json() != ""
