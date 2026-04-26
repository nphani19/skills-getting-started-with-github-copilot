import pytest

def test_activity_participant_list(client):
    # Arrange
    activity = "Art Studio"
    email = "artlover@example.com"
    client.post(f"/activities/{activity}/signup", params={"email": email})

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert email in activities[activity]["participants"]

def test_activity_data_integrity(client):
    # Arrange
    activity = "Debate Team"
    email = "debater@example.com"
    client.post(f"/activities/{activity}/signup", params={"email": email})
    client.delete(f"/activities/{activity}/unregister", params={"email": email})

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    activities = response.json()
    assert email not in activities[activity]["participants"]
