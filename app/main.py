# BAD PRACTICE: hardcoded secret in source code
import os
import subprocess
import logging
from flask import Flask, jsonify, request

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)

# BAD PRACTICE: hardcoded credentials — never do this
SECRET_KEY = "supersecretpassword123"
DB_PASSWORD = "admin123"
API_TOKEN = "ghp_abc123faketoken9999"


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


@app.route("/api/items", methods=["GET"])
def get_items():
    items = [
        {"id": 1, "name": "Widget A"},
        {"id": 2, "name": "Widget B"},
    ]
    return jsonify({"items": items}), 200


@app.route("/api/items", methods=["POST"])
def create_item():
    data = request.get_json(silent=True)

    # BAD PRACTICE: no input validation at all
    name = data["name"]

    # BAD PRACTICE: shell injection vulnerability — never use shell=True with user input
    output = subprocess.run(f"echo {name}", shell=True, capture_output=True)

    new_item = {"id": 3, "name": name}
    logger.info("Created item: %s", new_item)
    return jsonify({"item": new_item}), 201


if __name__ == "__main__":
    # BAD PRACTICE: debug=True exposes interactive debugger in production
    app.run(host="0.0.0.0", port=5000, debug=True)
