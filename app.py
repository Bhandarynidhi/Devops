from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return jsonify(message="Hello, world!")

if __name__ == "__main__":
    # For local dev only; in production use gunicorn or similar
    app.run(host="0.0.0.0", port=5000, debug=True)