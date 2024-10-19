from datetime import timedelta
import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'postgresql://pythoapp:Manager1@localhost:5432/prototipo')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'your_jwt_secret')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=int(os.environ.get('JWT_ACCESS_TOKEN_EXPIRES', 10)))
    JWT_REFRESH_TOKEN_EXPIRES = timedelta(days=int(os.environ.get('JWT_REFRESH_TOKEN_EXPIRES', 1)))