# app.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello Abhishek 🚀 — Flask running inside Docker on AWS!"

@app.route("/resume")
def resume():
    return "Resume link: https://drive.google.com/file/d/1QQ03fwdgbGayqC43gE7F8vNnJ73-8WnV/view?usp=drivesdk"

@app.route("/about")
def about():
    return jsonify({
        "name": "Abhishek Yadav",
        "role": "DevOps Engineer",
        "skills": ["AWS", "Docker", "CI/CD", "Kubernetes"],
        "message": "Containerization + AWS deployment + CI/CD."
    })

@app.route("/projects")
def projects():
    return jsonify([
        {"title": "Portfolio Website", "tech": "AWS S3 + CloudFront"},
        {"title": "Dockerized Flask App", "tech": "AWS ECR + ECS"},
        {"title": "CI/CD Pipeline", "tech": "GitHub Actions"}
    ])

@app.route("/health")
def health():
    return jsonify({"status": "UP"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
