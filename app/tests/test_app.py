from app import app

def test_root():
    client = app.test_client()
    res = client.get("/")
    assert res.status_code == 200
    assert "Deployed via Ansible" in res.get_json()["message"]
