import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_youtube_search():
    payload = {
        "song": "Bohemian Rhapsody",
        "artist": "Queen",
        "total_results": 1,
        "query_id": 1
    }
    response = client.post("/api/search", json=payload)
    assert response.status_code == 200, f"Status code was {response.status_code}, response: {response.text}"
    data = response.json()
    assert data["success"] is True
    assert "results" in data
    assert isinstance(data["results"], list)
    assert len(data["results"]) > 0
    assert "title" in data["results"][0]
    assert "video_id" in data["results"][0]
    assert "duration" in data["results"][0]
