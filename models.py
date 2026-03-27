# file: models.py
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(200))
    role = db.Column(db.String(20))


class FeedRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    feed_type = db.Column(db.String(100))
    quantity = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)


class Monitoring(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    larvae_growth = db.Column(db.Float)
    input_log = db.Column(db.String(200))
    output_log = db.Column(db.String(200))