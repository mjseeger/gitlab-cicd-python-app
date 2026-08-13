"""
A small Flask API used to demonstrate a full CI/CD pipeline with GitLab CI:
lint -> test -> build (Docker) -> push (GitLab Container Registry).
"""
from datetime import datetime, timezone

from flask import Flask, jsonify

app = Flask(__name__)

# In-memory "database" of tasks, just to have something slightly more
# interesting than a single hello-world endpoint.
TASKS = [
    {"id": 1, "title": "Learn Terraform", "done": True},
    {"id": 2, "title": "Set up a GitLab CI/CD pipeline", "done": False},
    {"id": 3, "title": "Add this project to my CV", "done": False},
]


@app.route("/health", methods=["GET"])
def health():
    """Simple health check endpoint used e.g. by container orchestrators."""
    return jsonify(status="ok"), 200


@app.route("/time", methods=["GET"])
def current_time():
    """Returns the current UTC time as ISO-8601."""
    return jsonify(utc_time=datetime.now(timezone.utc).isoformat()), 200


@app.route("/tasks", methods=["GET"])
def list_tasks():
    """Returns the list of tasks."""
    return jsonify(tasks=TASKS), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
