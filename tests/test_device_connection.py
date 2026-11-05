def test_disconnect_device(client):

    response = client.post('/device/disconnect')

    assert response.status_code == 200

    data = response.get_json()

    assert data["connected"] == False


def test_connect_device(client):

    response = client.post('/device/connect')

    assert response.status_code == 200

    data = response.get_json()

    assert data["connected"] == True


def test_device_status_after_disconnect(client):

    client.post('/device/disconnect')

    response = client.get('/device/status')

    data = response.get_json()

    assert data["connected"] == False
    assert data["online"] == False


def test_device_status_after_connect(client):

    client.post('/device/connect')

    response = client.get('/device/status')

    data = response.get_json()

    assert data["connected"] == True
    assert data["online"] == True


def test_change_speed_while_disconnected(client):

    client.post('/device/disconnect')

    response = client.post(
        '/device/speed',
        json={"speed": 4}
    )

    assert response.status_code == 409

    data = response.get_json()

    assert data["error"] == "Device is disconnected"