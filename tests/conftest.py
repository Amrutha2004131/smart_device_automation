import pytest
from app import app, device


@pytest.fixture
def client():

    # Reset device state before each test
    device["device_id"] = "FAN001"
    device["connected"] = True
    device["online"] = True
    device["fan_speed"] = 1
    device["temperature"] = 28

    app.config["TESTING"] = True

    with app.test_client() as client:

        yield client