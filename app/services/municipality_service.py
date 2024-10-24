from ..utils.validate_registers import ValidateRegister
from ..models.municipality_model import Municipality
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class MunicipalityService:


    def create_municipality(self, data, usr):
        try:
            if ValidateRegister.municipality_exists(data['muncipalidad']):
                return f"{constants.EXIST}{data['muncipalidad']}"
            else:
                validate = ValidateRegister.validate_departament_status(data['codDepartamento'])
                if validate == constants.Ok:    
                    new_municipality = Municipality (
                        nameMunicipality = data['muncipalidad'],
                        postalCode = data['postalCodigo'],
                        idDepartment = data['codDepartamento'],

                        status = constants.ENABLED,
                        usr_create = usr,
                        tim_create = datetime.now()
                    )
                    
                    db.session.add(new_municipality)
                    db.session.commit()

                    return f"{constants.CREATE}Municipality {data['muncipalidad']}"
                
                else:

                    return validate  
        
        except Exception as e:
            print('---------------> ERROR create_municipality: ---------------> ', e)
            return None
    

    def get_municipalities(self):
        read_municipalities = Municipality.query.all()
        if read_municipalities:
            data = {
                'municipalidades': [
                    {
                        'id': p.idMunicipality,
                        'muncipalidad': p.nameMunicipality,
                        'postalCodigo': p.postalCode,
                        'codDepartamento': p.idDepartment,
                        'estadoMunicipio': p.status
                    } for p in read_municipalities
                ]
            }
        else:
            return None

        return data
    

    def get_combo_municipalities(self, id):
        read_municipalities = Municipality.query.filter(
                                Municipality.idDepartment == id,
                                Municipality.status == constants.ENABLED)
        if read_municipalities.count() == 0:
            return None
        
        if read_municipalities:
            data = {
                'municipalidades': [
                    {
                        'id': p.idMunicipality,
                        'muncipalidad': p.nameMunicipality
                    } for p in read_municipalities
                ]
            }
                    
        return data
    

    def update_municipality(self, data, usr):
        try: 
            refresh_municipality = Municipality.query.filter_by(idMunicipality=data['id']).first()
            if refresh_municipality:    
                validate = ValidateRegister.validate_departament_status(data['codDepartamento'])   
                if validate == constants.Ok:             
                    if data['muncipalidad']: 
                        refresh_municipality.nameMunicipality = data['muncipalidad']
                    
                    if data['postalCodigo']:
                        refresh_municipality.postalCode = data['postalCodigo']
                    
                    if data['codDepartamento']:
                        refresh_municipality.idDepartment = data['codDepartamento']

                    if data['estadoMunicipio']:
                        refresh_municipality.status = data['estadoMunicipio']

                    refresh_municipality.usr_update = usr
                    refresh_municipality.tim_update = datetime.now()            
                    db.session.commit()

                    return f"{constants.UPDATE}Municipality {data['muncipalidad']}"
                
                else:
                    
                    return validate  
                
            return constants.NOT_FOUND

        except Exception as e:
            print('---------------> ERROR update_municipality: ---------------> ', e)
            return None