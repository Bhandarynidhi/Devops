from flask import Flask, jsonify, request
import platform
import sys
from datetime import datetime

APP_NAME = "DevSecOps Demo API"
VERSION = "0.1.0"
START_TIME = datetime.utcnow()

app = Flask(__name__)

@app.route("/")
def root():
    return jsonify({
        "app": APP_NAME,
        "version": VERSION,
        "message": "Welcome, Nidhi!"
    })

@app.route("/health")
def health():
    uptime_seconds = (datetime.utcnow() - START_TIME).total_seconds()
    return jsonify({
        "status": "ok",
        "uptime_seconds": int(uptime_seconds)
    })

@app.route("/info")
def info():
    return jsonify({
        "python": sys.version.split()[0],
        "platform": platform.system(),
        "platform_release": platform.release(),
        "server_time_utc": datetime.utcnow().isoformat() + "Z"
    })

@app.route("/echo", methods=["POST"])
def echo():
    # Return back whatever JSON was posted under the "echo" key
    try:
        data = request.get_json(force=True, silent=False)
    except Exception:
        return jsonify({"error": "invalid json"}), 400

    return jsonify({"echo": data})

@app.route("/todos")
def todos():
    # Example static list for demo / CI tests
    sample_todos = [
        {"id": 1, "task": "Write tests", "done": False},
        {"id": 2, "task": "Configure CI", "done": False},
        {"id": 3, "task": "Run security scan", "done": False}
    ]
    return jsonify({"todos": sample_todos})

if __name__ == "__main__":
    # For local development only
    app.run(host="0.0.0.0", port=5000, debug=True)
