from flask import Blueprint, request, jsonify, session
from database import get_connection

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    name = data.get("name")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (email, password, name) VALUES (?, ?, ?)", (email, password, name))
    conn.commit()
    conn.close()
    return jsonify({"message": "Signup successful!"})

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
    user = cursor.fetchone()
    conn.close()
    if user:
        session["user_id"] = user["id"]
        return jsonify({"message": "Login successful!"})
    return jsonify({"message": "Invalid credentials"}), 401
