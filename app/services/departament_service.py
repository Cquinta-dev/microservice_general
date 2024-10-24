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
                validate = ValidateRegister.validate_country_status(data['codPais'])
                if validate == constants.Ok:
                    new_departament = Departament (
                        nameDepartament = data['departamento'],
                        headboardDepartament = data['cabecera'],
                        postalCode = data['postalCodigo'],
                        idCountry = data['codPais'],

                        status = constants.ENABLED,
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
                        'id': p.idDepartment,
                        'departamento': p.nameDepartament,
                        'cabecera': p.headboardDepartament,
                        'postalCodigo': p.postalCode,
                        'codPais': p.idCountry,
                        'estadoDepartamento': p.status,
                    } for p in read_departaments
                ]
            }
        else:

            return None

        return data


    def get_combo_departament(self, id):
        read_departaments = Departament.query.filter(
                                Departament.idCountry == id,
                                Departament.status == constants.ENABLED)
        if read_departaments.count() == 0:
            return None
        
        if read_departaments:
            data = {
                'departamentos': [
                    {
                        'id': p.idDepartment,
                        'departamento': p.nameDepartament
                    } for p in read_departaments
                ]
            }
        
        return data


    def update_departament(self, data, usr):
        try:
            refresh_departament = Departament.query.filter_by(idDepartment=data['id']).first()
            if refresh_departament:
                validate = ValidateRegister.validate_country_status(data['codPais'])   
                if validate == constants.Ok:      
                    if data['departamento']: 
                        refresh_departament.nameDepartament = data['departamento']
                    
                    if data['cabecera']:
                        refresh_departament.headboardDepartament = data['cabecera']
                    
                    if data['postalCodigo']:
                        refresh_departament.postalCode = data['postalCodigo']

                    if data['codPais']:
                        refresh_departament.idCountry = data['codPais']

                    if data['estadoDepartamento']:
                        refresh_departament.status = data['estadoDepartamento']

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