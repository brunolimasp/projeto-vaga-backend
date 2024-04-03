from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_employees():
    response = client.get("/employee/list?department=Engenharia")
    assert response.status_code == 200
