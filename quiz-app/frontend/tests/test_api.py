from fastapi.testclient import TestClient
from api.endpoints import app

client = TestClient(app)

def test_generate_quiz_endpoint():
    response = client.post("/generate-quiz", json={
        "text": "The sun is the star at the center of the Solar System.",
        "num_questions": 2
    })
    assert response.status_code == 200
    assert "quiz" in response.json()
    assert isinstance(response.json()["quiz"], str)
