from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.currency_schema import expected_fields_create

currency_routes = Blueprint('currency', __name__)

#Method for create person.
@currency_routes.route('/createCurrency',methods=['POST'])
#@jwt_required()
def create_currency():

    try:        
        data = request.get_json(force=True)
        if data is None:
            return jsonify({'error': 'No JSON data provided'}), 400
        
        missing_fields = expected_fields_create - data.keys()
        if missing_fields:
            return jsonify({'error': 'Missing fields', 'missing': list(missing_fields)}), 400
        
        currencyCreate = service_manager.currency_service.create_currency(data, 'root')#get_jwt_identity())
        if currencyCreate is None:
            return jsonify({'error': 'Internal Server'}), 500   
        
        return jsonify({'message': 'Currency created'}), 201
    
    except Exception as e:
        print(e)
        return jsonify({'error': 'Internal Server'}), 500    