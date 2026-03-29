# config.py
import os

class Config:
    SQLALCHEMY_DATABASE_URI = "sqlite:///bsf.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET", "super-long-and-secure-secret-key-1234567890")