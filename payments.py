from flask import Blueprint, request, jsonify
from database import get_connection
import requests

payments_bp = Blueprint("payments", __name__)

# Dubai Bank Payment
@payments_bp.route("/pay/dubai-bank", methods=["POST"])
def pay_dubai_bank():
    data = request.json
    amount = data.get("amount")
    order_id = data.get("order_id")
    
    response = requests.post("https://dubai-bank-api.com/pay", json={
        "order_id": order_id,
        "amount": amount,
        "currency": "AED"
    })
    
    result = response.json()
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO payments (order_id, method, amount, status) VALUES (?, ?, ?, ?)",
                   (order_id, "Dubai Bank", amount, result.get("status", "pending")))
    conn.commit()
    conn.close()
    
    return jsonify(result)

# Tabby Payment (Buy Now, Pay Later)
@payments_bp.route("/pay/tabby", methods=["POST"])
def pay_tabby():
    data = request.json
    amount = data.get("amount")
    order_id = data.get("order_id")
    
    response = requests.post("https://api.tabby.ai/v1/checkout", json={
        "order_id": order_id,
        "amount": amount,
        "currency": "AED"
    }, headers={"Authorization": "Bearer YOUR_TABBY_SECRET_KEY"})
    
    result = response.json()
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO payments (order_id, method, amount, status) VALUES (?, ?, ?, ?)",
                   (order_id, "Tabby", amount, result.get("status", "pending")))
    conn.commit()
    conn.close()
    
    return jsonify(result)

# Initialize payments table
def init_payments_table():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_id TEXT,
            method TEXT,
            amount REAL,
            status TEXT
        )
    """)
    conn.commit()
    conn.close()

init_payments_table()
