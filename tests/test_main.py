from app.main import app


def test_home():
    client = app.test_client()
    response = client.get("/")

    assert response.status_code == 200
    assert b"Welcome to the DevSecOps Demo Application" in response.data


def test_health():
    client = app.test_client()
    response = client.get("/health")

    assert response.status_code == 200
    assert b"healthy" in response.data


def test_message():
    client = app.test_client()
    response = client.get("/api/message")

    assert response.status_code == 200
    assert b"DevSecOps pipeline is working!" in response.data
