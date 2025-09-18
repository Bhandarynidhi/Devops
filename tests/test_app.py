from app import app

def test_root():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert resp.get_json() == {
        "app": "DevSecOps Demo API",
        "version": "0.1.0",
        "message": "Welcome, Nidhi!"
    }

def test_health():
    client = app.test_client()
    resp = client.get("/health")
    assert resp.status_code == 200
    j = resp.get_json()
    assert j["status"] == "ok"
    assert "uptime_seconds" in j

def test_info():
    client = app.test_client()
    resp = client.get("/info")
    assert resp.status_code == 200
    j = resp.get_json()
    assert "python" in j
    assert "platform" in j

def test_echo():
    client = app.test_client()
    payload = {"hello": "world"}
    resp = client.post("/echo", json=payload)
    assert resp.status_code == 200
    assert resp.get_json() == {"echo": payload}

def test_todos():
    client = app.test_client()
    resp = client.get("/todos")
    assert resp.status_code == 200
    j = resp.get_json()
    assert "todos" in j
    assert isinstance(j["todos"], list)
