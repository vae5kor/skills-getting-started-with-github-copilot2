"""
Tests for multiplication table functionality
"""

from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)


def test_multiplication_table_basic():
    """Test basic multiplication table generation"""
    response = client.get("/multiplication-table/5")
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == 5
    assert len(data["table"]) == 10
    assert data["table"][0] == "5 x 1 = 5"
    assert data["table"][4] == "5 x 5 = 25"
    assert data["table"][9] == "5 x 10 = 50"


def test_multiplication_table_one():
    """Test multiplication table for 1"""
    response = client.get("/multiplication-table/1")
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == 1
    assert data["table"][0] == "1 x 1 = 1"
    assert data["table"][9] == "1 x 10 = 10"


def test_multiplication_table_large_number():
    """Test multiplication table for larger number"""
    response = client.get("/multiplication-table/12")
    assert response.status_code == 200
    data = response.json()
    assert data["number"] == 12
    assert data["table"][0] == "12 x 1 = 12"
    assert data["table"][9] == "12 x 10 = 120"


def test_multiplication_table_negative_number():
    """Test that negative numbers return error"""
    response = client.get("/multiplication-table/-5")
    assert response.status_code == 400
    assert "Number must be positive" in response.json()["detail"]


def test_multiplication_table_zero():
    """Test that zero returns error"""
    response = client.get("/multiplication-table/0")
    assert response.status_code == 400
    assert "Number must be positive" in response.json()["detail"]
