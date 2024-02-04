

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    obj = response.get_json()
    assert obj['message'] == 'Hello, World!'
    
    
