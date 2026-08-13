import pytest

from app.main import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health_endpoint_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_time_endpoint_returns_iso_timestamp(client):
    response = client.get("/time")
    assert response.status_code == 200
    body = response.get_json()
    assert "utc_time" in body
    # A very loose sanity check that it looks like an ISO-8601 timestamp
    assert "T" in body["utc_time"]


def test_tasks_endpoint_returns_three_tasks(client):
    response = client.get("/tasks")
    assert response.status_code == 200
    body = response.get_json()
    assert "tasks" in body
    assert len(body["tasks"]) == 3
    assert body["tasks"][0]["title"] == "Learn Terraform"
