from flask import Blueprint, request, jsonify

discounts_bp = Blueprint("discounts", __name__)

# Example discount logic
@discounts_bp.route("/apply", methods=["POST"])
def apply_discount():
    data = request.json
    product_id = data.get("product_id")
    discount_percent = data.get("discount_percent", 0)
    # Placeholder logic
    discounted_price = f"Discount applied: {discount_percent}% for product {product_id}"
    return jsonify({"message": discounted_price})
