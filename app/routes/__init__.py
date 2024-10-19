from flask import Blueprint
from .person_routes import person_routes

main_routes = Blueprint('main', __name__)

# Registra los blueprints
main_routes.register_blueprint(person_routes)

@main_routes.route('/')
def index():
    return {"message": "Welcome to the API!"}