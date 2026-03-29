# file: routes.py
from flask import Blueprint, request, jsonify
from models import db, User, FeedRecord, Monitoring
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    create_access_token, jwt_required, get_jwt_identity
)

api = Blueprint("api", __name__)

@api.route("/register", methods=["POST"])
def register():
    data = request.json
    user = User(
        name=data["name"],
        email=data["email"],
        password=generate_password_hash(data["password"]),
        role=data.get("role", "farmer"),
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201


@api.route("/login", methods=["POST"])
def login():
    data = request.json
    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password_hash(user.password, data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    # Convert user ID to string for JWT
    token = create_access_token(identity=str(user.id))
    return jsonify({"access_token": token})


@api.route("/feed", methods=["POST"])
@jwt_required()
def create_feed():
    # Convert JWT identity back to int
    user_id = int(get_jwt_identity())
    data = request.json

    record = FeedRecord(
        user_id=user_id,
        feed_type=data["feed_type"],
        quantity=data["quantity"],
    )
    db.session.add(record)
    db.session.commit()

    return jsonify({"msg": "Feed added"})


@api.route("/feed", methods=["GET"])
@jwt_required()
def get_feed():
    # Convert JWT identity back to int
    user_id = int(get_jwt_identity())
    records = FeedRecord.query.filter_by(user_id=user_id).all()

    return jsonify([
        {"type": r.feed_type, "quantity": r.quantity}
        for r in records
    ])


@api.route("/monitor", methods=["POST"])
@jwt_required()
def create_monitor():
    # Convert JWT identity back to int
    user_id = int(get_jwt_identity())
    data = request.json

    log = Monitoring(
        user_id=user_id,
        larvae_growth=data["larvae_growth"],
        input_log=data["input_log"],
        output_log=data["output_log"],
    )
    db.session.add(log)
    db.session.commit()

    return jsonify({"msg": "Monitoring saved"})