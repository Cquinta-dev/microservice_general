from ..utils.validate_registers import ValidateRegister
from ..models.departament_model import Departament
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class DepartamentService:


    def create_departament(self, data, usr):
        try:            
            if ValidateRegister.departament_exists(data['departamento']):
                return f"{constants.EXIST}{data['departamento']}"
            else:
                validate = ValidateRegister.validate_country_status(data['IdPais'])
                if validate == constants.Ok:
                    new_departament = Departament (
                        nameDepartament = data['departamento'],
                        headboardDepartament = data['cabecera'],
                        postalCode = data['postalCodigo'],
                        codeCountry = data['IdPais'],

                        status_dep = constants.ENABLED,
                        usr_create = usr,
                        tim_create = datetime.now()
                    )            
                    db.session.add(new_departament)
                    db.session.commit()

                    return f"{constants.CREATE}Departament {data['departamento']}"
                
                else:

                    return validate    
                
        except Exception as e:
            print('---------------> ERROR create_departament: ---------------> ', e)
            return None
    

    def get_departaments(self):
        read_departaments = Departament.query.all()
        if read_departaments:
            data = {
                'departamentos': [
                    {
                        'id': p.codeDepartment,
                        'departamento': p.nameDepartament,
                        'cabecera': p.headboardDepartament,
                        'postalCodigo': p.postalCode,
                        'IdPais': p.codeCountry,
                        'estadoDepartamento': p.status_dep,
                    } for p in read_departaments
                ]
            }
        else:

            return None

        return data


    def get_combo_departament(self, id):
        read_departaments = Departament.query.filter(
                                Departament.codeCountry == id,
                                Departament.status_dep == constants.ENABLED)
        if read_departaments.count() == 0:
            return None
        
        if read_departaments:
            data = {
                'departamentos': [
                    {
                        'id': p.codeDepartment,
                        'departamento': p.nameDepartament
                    } for p in read_departaments
                ]
            }
        
        return data


    def update_departament(self, data, usr):
        try:
            refresh_departament = Departament.query.filter_by(codeDepartment=data['id']).first()
            if refresh_departament:
                validate = ValidateRegister.validate_country(data['IdPais'])   
                if validate == constants.Ok:      
                    if data['departamento']: 
                        refresh_departament.nameDepartament = data['departamento']
                    
                    if data['cabecera']:
                        refresh_departament.headboardDepartament = data['cabecera']
                    
                    if data['postalCodigo']:
                        refresh_departament.postalCode = data['postalCodigo']

                    if data['IdPais']:
                        refresh_departament.codeCountry = data['IdPais']

                    if data['estadoDepartamento']:
                        refresh_departament.status_dep = data['estadoDepartamento']

                    refresh_departament.usr_update = usr
                    refresh_departament.tim_update = datetime.now()            
                    db.session.commit()
                    
                    return f"{constants.UPDATE}Departament {data['departamento']}"
                
                else:
                    
                    return validate  
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_currency: ---------------> ', e)
            return None    