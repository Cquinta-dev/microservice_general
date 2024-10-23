from app.models.departament_model import Departament
from app.database import db
from datetime import datetime
from ..utils.constants import constants

class DepartamentService:


    def create_departament(self, data, usr):
        try:
            new_departament = Departament (
                nameDepartament = data['departamento'],
                headboardDepartament = data['cabecera'],
                postalCode = data['postalCodigo'],
                codeNumeric = data['idPais'],

                status_dep = 'E',
                usr_create = usr,
                tim_create = datetime.now()
            )
            
            db.session.add(new_departament)
            db.session.commit()

            return new_departament
        
        except Exception as e:
            print('---------------> ERROR create_departament: ---------------> ', e)
            return None
    

    def get_all_departaments(self):
        read_departaments = Departament.query.all()
        if read_departaments:
            data = {
                'departamentos': [
                    {
                        'id': p.codeDepartment,
                        'departamento': p.nameDepartament,
                        'cabecera': p.headboardDepartament,
                        'postalCodigo': p.postalCode,
                        'idPais': p.codeNumeric,
                        'estadoDepartamento': p.status_dep,
                    } for p in read_departaments
                ]
            }
        else:
            return None

        return data


    def get_departament(self, id):
        read_departament = Departament.query.filter_by(codeDepartment=id).first()
        if read_departament:
            data = {
                'id': id,
                'departamento': read_departament.nameDepartament,
                'cabecera': read_departament.headboardDepartament,
                'postalCodigo': read_departament.postalCode,
                'idPais': read_departament.codeNumeric,
                'estadoDepartamento': read_departament.status_dep
            }
        else:
            return None

        return data 


    def update_departament(self, data, usr):
        try:
            refresh_departament = Departament.query.filter_by(codeDepartment=data['id']).first()
            if refresh_departament:            
                if data['departamento']: 
                    refresh_departament.nameDepartament = data['departamento']
                
                if data['cabecera']:
                    refresh_departament.headboardDepartament = data['cabecera']
                
                if data['postalCodigo']:
                    refresh_departament.postalCode = data['postalCodigo']

                if data['idPais']:
                    refresh_departament.codeNumeric = data['idPais']

                if data['estadoDepartamento']:
                    refresh_departament.status_dep = data['estadoDepartamento']

                refresh_departament.usr_update = usr
                refresh_departament.tim_update = datetime.now()            
                db.session.commit()

                return refresh_departament
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_currency: ---------------> ', e)
            return None