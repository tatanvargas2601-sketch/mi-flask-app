from wsgi import app


def test_health_responde_200():
    response = app.test_client().get("/health")
    assert response.status_code == 200

def test_home():
    client = create_app().test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Hola desde staging"