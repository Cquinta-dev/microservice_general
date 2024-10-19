from flask_jwt_extended import JWTManager
from flask import Flask
from .config import Config
from .database import db
from .routes import main_routes

def create_app():
    
    app = Flask(__name__)
    app.register_blueprint(main_routes)
    app.config.from_object(Config)
    JWTManager(app)

    db.init_app(app)
    with app.app_context():
        #db.drop_all()
        db.create_all()

    return app