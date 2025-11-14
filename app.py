from flask import Flask
from auth import auth_bp
from products import products_bp
from discounts import discounts_bp

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Register Blueprints
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(products_bp, url_prefix="/products")
app.register_blueprint(discounts_bp, url_prefix="/discounts")

@app.route("/")
def home():
    return "Welcome to Mohammed Hamdan AlShehhi Ladies Tailoring & Embroidery Backend"

if __name__ == "__main__":
    app.run(debug=True)
