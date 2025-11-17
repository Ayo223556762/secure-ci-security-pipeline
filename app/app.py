from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def health():
    return jsonify({"status": "ok", "message": "Secure CI pipeline demo"})

@app.route("/secret-check")
def secret_check():
    db_password = os.getenv("DB_PASSWORD", "not_set")
    return jsonify({"db_password_is_set": db_password != "not_set"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
