from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data == b'Hello! This is Python 2.7.18'
    assert response.status_code == 200
