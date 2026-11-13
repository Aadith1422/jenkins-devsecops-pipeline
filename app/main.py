from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to the DevSecOps Demo Application"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/api/message")
def message():
    return jsonify({
        "message": "DevSecOps pipeline is working!"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

