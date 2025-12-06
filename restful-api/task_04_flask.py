#!/usr/bin/python3
"""
A simple Flask API example.
Supports GET and POST requests to manage users.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory users dictionary
users = {}

# Root endpoint
@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"

# Status endpoint
@app.route("/status", methods=["GET"])
def status():
    return "OK"

# Data endpoint: return list of usernames
@app.route("/data", methods=["GET"])
def data():
    return jsonify(list(users.keys()))

# User endpoint: get full user info
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Add user endpoint: POST request
@app.route("/add_user", methods=["POST"])
def add_user():
    try:
        data = request.get_json(force=True)
    except:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # Add user to dictionary
    user_info = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    users[username] = user_info

    return jsonify({"message": "User added", "user": user_info}), 201

# Run the app
if __name__ == "__main__":
    app.run()
