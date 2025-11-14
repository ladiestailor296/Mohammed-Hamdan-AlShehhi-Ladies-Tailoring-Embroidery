from flask import Blueprint, request, jsonify
from database import get_connection

products_bp = Blueprint("products", __name__)

@products_bp.route("/add", methods=["POST"])
def add_product():
    data = request.json
    name = data.get("name")
    description = data.get("description")
    price = data.get("price")
    image_url = data.get("image_url")
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO products (name, description, price, image_url) VALUES (?, ?, ?, ?)",
                   (name, description, price, image_url))
    conn.commit()
    conn.close()
    return jsonify({"message": "Product added successfully!"})

@products_bp.route("/list", methods=["GET"])
def list_products():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM products")
    products = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return jsonify(products)
