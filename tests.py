from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert response.data.startswith('Hello! This is Python 2')
    assert response.data.startswith('Hello! This is Python 2')
    assert response.status_code == 200
