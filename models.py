# file: models.py
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False, index=True)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20), default="farmer")

    # Relationships
    feeds = db.relationship("FeedRecord", backref="user", lazy=True)
    monitors = db.relationship("Monitoring", backref="user", lazy=True)
    audit_logs = db.relationship("AuditLog", backref="user", lazy=True)  # NEW


class FeedRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    feed_type = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)


class Monitoring(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)
    larvae_growth = db.Column(db.Float, nullable=False)
    input_log = db.Column(db.String(200))
    output_log = db.Column(db.String(200))
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, index=True)  # Linked to User
    action = db.Column(db.String(200), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow, index=True)