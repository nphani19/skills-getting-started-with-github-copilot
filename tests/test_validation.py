import pytest

def test_signup_duplicate(client):
    # Arrange
    activity = "Programming Class"
    email = "dup@example.com"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"].lower()

def test_unregister_not_registered(client):
    # Arrange
    activity = "Programming Class"
    email = "notregistered@example.com"

    # Act
    response = client.delete(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 400
    assert "not registered" in response.json()["detail"].lower()

def test_unregister_nonexistent_activity(client):
    # Arrange
    activity = "Nonexistent"
    email = "someone@example.com"

    # Act
    response = client.delete(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()
