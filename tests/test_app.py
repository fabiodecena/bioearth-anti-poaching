from app import app


def test_home():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.data == b"Protect Wildlife!!! v5"


def test_health():
    client = app.test_client()

    response = client.get("/health")

    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "v3"}


def test_version():
    client = app.test_client()

    response = client.get("/version")

    assert response.status_code == 200
    assert response.get_json() == {"version": "v3"}