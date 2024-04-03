from fastapi.testclient import TestClient

from ..main import app

client = TestClient(app)


def test_department():
    response = client.get("/department/list")
    assert response.status_code == 200
    assert response.json() == [
        {"department": "Marketing"},
        {"department": "Desenvolvimento"},
        {"department": "Recursos Humanos"},
        {"department": "Vendas"},
        {"department": "Suporte Técnico"},
        {"department": "Financeiro"},
        {"department": "Produção"},
        {"department": "Engenharia"},
        {"department": "Atendimento ao Cliente"},
        {"department": "Administração"},
    ]
