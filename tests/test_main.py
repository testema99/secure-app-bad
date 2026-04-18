import pytest
from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


# BAD PRACTICE: test only checks status code, not response content
def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200


# BAD PRACTICE: this test is completely wrong — asserts 404 on a valid route
def test_get_items_wrong(client):
    response = client.get("/api/items")
    assert response.status_code == 404   # WRONG: real answer is 200


# BAD PRACTICE: test passes bad data and expects success — will fail
def test_create_item_no_data(client):
    response = client.post(
        "/api/items",
        json={},                         # missing 'name' — will cause a KeyError crash
        content_type="application/json",
    )
    assert response.status_code == 201  # WRONG: will get 500
