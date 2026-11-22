from wsgi import app


def test_health_con_mysql():
    response = app.test_client().get("/health")
    assert response.status_code == 200
