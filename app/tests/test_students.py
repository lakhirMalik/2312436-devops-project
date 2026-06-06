def test_post_student(client):
    response = client.post("/students", json={
        "name": "Ali Khan",
        "reg_no": "FA21-BCS-001",
        "email": "ali@example.com"
    })
    assert response.status_code == 201
    data = response.json()
    assert data["reg_no"] == "FA21-BCS-001"
    assert "id" in data


def test_get_students(client):
    client.post("/students", json={
        "name": "Sara Ahmed",
        "reg_no": "FA21-BCS-002"
    })
    response = client.get("/students")
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_get_student_by_reg_no(client):
    client.post("/students", json={
        "name": "Usman Malik",
        "reg_no": "FA21-BCS-003"
    })
    response = client.get("/students/FA21-BCS-003")
    assert response.status_code == 200
    assert response.json()["name"] == "Usman Malik"


def test_get_student_not_found(client):
    response = client.get("/students/FAKE-999")
    assert response.status_code == 404


def test_duplicate_reg_no(client):
    client.post("/students", json={"name": "A", "reg_no": "DUP-001"})
    response = client.post("/students", json={"name": "B", "reg_no": "DUP-001"})
    assert response.status_code == 400
