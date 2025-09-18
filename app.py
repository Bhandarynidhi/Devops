from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

# Dummy credentials (in real projects, store securely in DB or Vault)
VALID_USERNAME = "admin"
VALID_PASSWORD = "secret123"

@app.route("/")
def hello():
    return jsonify(
        message="Hello, DevSecOps!",
        start_time=datetime.utcnow().isoformat()
    )

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username == VALID_USERNAME and password == VALID_PASSWORD:
        return jsonify(status="success", message="Login successful")
    else:
        return jsonify(status="failure", message="Invalid credentials"), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
