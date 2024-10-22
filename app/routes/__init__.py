from flask import Blueprint
from .country_routes import country_routes
from .departament_routes import departament_routes
from .municipality_routes import municipality_routes
from .currency_routes import currency_routes
from .company_routes import company_routes
from .person_routes import person_routes


main_routes = Blueprint('main', __name__)

# Registra los blueprints
main_routes.register_blueprint(country_routes)
main_routes.register_blueprint(departament_routes)
main_routes.register_blueprint(municipality_routes)
main_routes.register_blueprint(currency_routes)
main_routes.register_blueprint(company_routes)
main_routes.register_blueprint(person_routes)

@main_routes.route('/')
def index():
    return {"message": "Welcome to the API!"}