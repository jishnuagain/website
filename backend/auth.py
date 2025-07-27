from flask import Blueprint, request, jsonify
from models import User, db
from extensions import db
from models import Order

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "User already exists"}), 409

    user = User(name=name, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201


@auth_bp.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        return jsonify({
            "message": "Login successful",
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
        })
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route('/api/orders', methods=['POST'])
def create_order():
    data = request.get_json()

    try:
        order = Order(
            product_id=data['id'],
            title=data['title'],
            image_url=data['image_url'],
            price=data['price'],
            quantity=data['quantity']
        )
        db.session.add(order)
        db.session.commit()

        return jsonify({"message": "Order placed successfully", "order_id": order.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

