import pytest

# Arrange-Act-Assert pattern is used in all tests

def test_get_activities(client):
    # Arrange
    # (client fixture provides the test client)

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, dict)
    assert len(data) > 0
    # Check that each activity has required fields
    for activity in data.values():
        assert "description" in activity
        assert "schedule" in activity
        assert "max_participants" in activity
        assert "participants" in activity

def test_signup_valid(client):
    # Arrange
    activity = "Chess Club"
    email = "testuser@example.com"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"].startswith("Signed up")

def test_signup_nonexistent_activity(client):
    # Arrange
    activity = "Nonexistent"
    email = "testuser2@example.com"

    # Act
    response = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert response.status_code == 404
    assert "not found" in response.json()["detail"].lower()

def test_unregister_valid(client):
    # Arrange
    activity = "Chess Club"
    email = "testuser@example.com"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    response = client.delete(f"/activities/{activity}/unregister", params={"email": email})

    # Assert
    assert response.status_code == 200
    assert response.json()["message"].startswith("Unregistered")
