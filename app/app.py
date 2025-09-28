from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def root():
    env = os.getenv("ENV_NAME", "local")
    sha = os.getenv("GIT_SHA", "dev")
    return jsonify(message=f"Deployed via Ansible ({env})", commit=sha)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
