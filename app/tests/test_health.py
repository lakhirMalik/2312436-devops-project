def test_health_returns_ok(client):
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_health_has_student_field(client):
    response = client.get("/health")
    data = response.json()
    assert "student" in data
    assert data["student"] != ""


def test_health_has_db_field(client):
    response = client.get("/health")
    data = response.json()
    assert "db" in data
