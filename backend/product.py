from flask import Blueprint, jsonify
from models import Product
from extensions import db

product_bp = Blueprint("product", __name__)

@product_bp.route("/api/products/<int:product_id>", methods=["GET"])
def get_product_by_id(product_id):
    product = Product.query.get(product_id)

    if not product:
        return jsonify({"error": "Product not found"}), 404

    return jsonify({
        "id": product.id,
        "title": product.title,
        "image_url": product.image_url,
        "original_price": str(product.original_price),
        "current_price": str(product.current_price),
        "in_stock": product.in_stock,
        "sizes": product.sizes.split(",") if product.sizes else [],
        "description": product.description,
        "features": product.features.split(",") if product.features else []
    })
