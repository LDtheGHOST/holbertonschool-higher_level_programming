#!/usr/bin/python3
from flask import Flask, jsonify, request
import json


app = Flask(__name__)
users = {}


@app.route('/')
def hello():
    return "Welcome to the Flask API !"


@app.route('/data')
def data():
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    return "OK"


@app.route('/users/<username>')
def user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    new_data = request.get_json()
    username = new_data.get('username')
    if not username:
        return jsonify({"error": "Username required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": new_data.get("name"),
        "age": new_data.get("age"),
        "city": new_data.get("city")
    }
    return jsonify({
        "message": "User added",
        "user": new_data
    }), 201


if __name__ == "__main__":
    app.run()