import pytest


def user_payload(
    name="Paul",
    email="paul@example.com",
    age=25,
    student_id="S1234567",
):
    return {
        "name": name,
        "email": email,
        "age": age,
        "student_id": student_id,
    }


def test_health_endpoint(client):
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_user_returns_201(client):
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Paul"
    assert data["email"] == "paul@example.com"


def test_duplicate_user_returns_409(client):
    client.post("/api/users", json=user_payload())
    response = client.post("/api/users", json=user_payload())

    assert response.status_code == 409
    assert "exists" in response.json()["detail"].lower()


@pytest.mark.parametrize(
    "bad_student_id",
    ["123456", "s1234567", "S123", "S12345678"],
)
def test_bad_student_id_returns_422(client, bad_student_id):
    response = client.post(
        "/api/users",
        json=user_payload(student_id=bad_student_id),
    )

    assert response.status_code == 422


def test_get_users_returns_created_users(client):
    client.post(
        "/api/users",
        json=user_payload(name="Alice", email="alice@example.com"),
    )
    response = client.get("/api/users")

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]["name"] == "Alice"


def test_get_existing_user_returns_200(client):
    created = client.post("/api/users", json=user_payload())
    user_id = created.json()["id"]

    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 200
    assert response.json()["id"] == user_id


def test_get_missing_user_returns_404(client):
    response = client.get("/api/users/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_delete_existing_user_returns_204(client):
    created = client.post("/api/users", json=user_payload())
    user_id = created.json()["id"]

    response = client.delete(f"/api/users/{user_id}")

    assert response.status_code == 204
    assert response.content == b""


def test_delete_missing_user_returns_404(client):
    response = client.delete("/api/users/999")

    assert response.status_code == 404
    assert response.json()["detail"] == "User not found"


def test_deleted_user_can_no_longer_be_retrieved(client):
    created = client.post("/api/users", json=user_payload())
    user_id = created.json()["id"]
    client.delete(f"/api/users/{user_id}")

    response = client.get(f"/api/users/{user_id}")

    assert response.status_code == 404
