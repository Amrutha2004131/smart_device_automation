def test_update_speed(client):

    response = client.post(
        '/device/speed',
        json={"speed": 3}
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["fan_speed"] == 3


def test_minimum_speed(client):

    response = client.post(
        '/device/speed',
        json={"speed": 1}
    )

    assert response.status_code == 200


def test_maximum_speed(client):

    response = client.post(
        '/device/speed',
        json={"speed": 5}
    )

    assert response.status_code == 200


def test_invalid_speed(client):

    response = client.post(
        '/device/speed',
        json={"speed": 8}
    )

    assert response.status_code == 400


def test_invalid_speed_type(client):

    response = client.post(
        '/device/speed',
        json={"speed": "high"}
    )

    assert response.status_code == 400