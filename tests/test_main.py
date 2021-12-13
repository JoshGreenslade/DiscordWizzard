from .fixtures import client

def test_root(client):
    res = client.get('/')
    message = res.json()['message']

    assert message
    assert res.status_code == 200
    