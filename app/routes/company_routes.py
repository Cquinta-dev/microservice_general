from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import Blueprint, jsonify, request
from app.services import service_manager
from ..schemas.company_schema import expected_fields_create
from ..schemas.company_schema import expected_fields_update
from ..utils.constants import constants

company_routes = Blueprint('company', __name__)

#Method for create person.
@company_routes.route('/createCompany',methods=['POST'])
@jwt_required()
def create_company():
   
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
    
    missing_fields = expected_fields_create - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400
    
    createCompany = service_manager.company_service.create_company(data, get_jwt_identity())
    if createCompany is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500   
    
    return jsonify({'message': 'Company created'}), 201


#Method for get list to companies.
@company_routes.route('/allCompanies', methods=['GET'])
@jwt_required()
def get_all_companies():

    allCompanies = service_manager.company_service.get_all_companies()
    if allCompanies is None:
        return jsonify({'error': constants.NOT_FOUND_LIST}), 404

    return jsonify(allCompanies), 200    


#Method for get one company.
@company_routes.route('/getCompany', methods=['GET'])
@jwt_required()
def get_company():

    id = request.args.get('id')
    if id is None: 
        return jsonify({'error': constants.NOT_ID}), 400
    
    getCompany = service_manager.company_service.get_company(id)
    if getCompany is None:
        return jsonify({'error':'Company not found'}), 404
    
    return jsonify(getCompany), 200


#Method for udpate company.
@company_routes.route('/updateCompany', methods=['PUT'])
@jwt_required()
def update_company():    
    
    data = request.get_json(force=True)
    if data is None:
        return jsonify({'error': constants.NOT_JSON}), 400
        
    missing_fields = expected_fields_update - data.keys()
    if missing_fields:
        return jsonify({'error': constants.NOT_FIELDS, 'missing': list(missing_fields)}), 400

    updateCompany = service_manager.company_service.update_company(data, get_jwt_identity())
    if updateCompany is constants.NOT_FOUND:
        return jsonify({'error':'Company not found'}), 404
    
    if updateCompany is None:
        return jsonify({'error': constants.INTERNAL_ERROR}), 500        
        
    return jsonify({'message': 'Company updated'}), 201