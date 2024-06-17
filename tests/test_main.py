import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from fastapi.testclient import TestClient
from main import app, init_db

client = TestClient(app)

# Initialisation de la base de données pour les tests
init_db()

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the FastAPI RPN Calculator API!"}

def test_evaluate_addition():
    response = client.post("/evaluate/", json={"expression": "3 4 +"})
    assert response.status_code == 200
    assert response.json() == {"expression": "3 4 +", "result": 7.0}

def test_evaluate_multiplication():
    response = client.post("/evaluate/", json={"expression": "3 4 *"})
    assert response.status_code == 200
    assert response.json() == {"expression": "3 4 *", "result": 12.0}

def test_evaluate_division():
    response = client.post("/evaluate/", json={"expression": "8 4 /"})
    assert response.status_code == 200
    assert response.json() == {"expression": "8 4 /", "result": 2.0}

def test_evaluate_invalid_expression():
    response = client.post("/evaluate/", json={"expression": "3 4 &"})
    assert response.status_code == 400

def test_export_data():
    response = client.get("/export/")
    assert response.status_code == 200
    assert response.json()["message"].startswith("Data exported to")

def test_download_file():
    response = client.get("/download/")
    assert response.status_code == 200
    assert "text/csv" in response.headers["content-type"]
    assert response.headers["content-disposition"].startswith("attachment; filename=")
