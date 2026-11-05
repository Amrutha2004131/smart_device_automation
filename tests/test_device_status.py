def test_device_status(client):

    response = client.get('/device/status')

    assert response.status_code == 200

    data = response.get_json()

    assert data["device_id"] == "FAN001"

    assert data["connected"] == True

    assert data["online"] == True

    assert data["fan_speed"] == 1