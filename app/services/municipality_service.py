from app.models.municipality_model import Municipality
from app.database import db
from datetime import datetime
from ..utils.constants import constants

class MunicipalityService:


    def create_municipality(self, data, usr):
        try:
            new_municipality = Municipality (
                nameMunicipality = data['muncipalidad'],
                postalCode = data['postalCodigo'],
                codeDepartment = data['IdDepartamento'],

                status_mun = 'E',
                usr_create = usr,
                tim_create = datetime.now()
            )
            
            db.session.add(new_municipality)
            db.session.commit()

            return new_municipality
        
        except Exception as e:
            print('---------------> ERROR create_municipality: ---------------> ', e)
            return None
    

    def get_all_municipalities(self):
        read_municipalities = Municipality.query.all()
        if read_municipalities:
            data = {
                'municipalidades': [
                    {
                        'id': p.codeMunicipality,
                        'muncipalidad': p.nameMunicipality,
                        'postalCodigo': p.postalCode,
                        'IdDepartamento': p.codeDepartment,
                        'estadoMunicipio': p.status_mun
                    } for p in read_municipalities
                ]
            }
        else:
            return None

        return data
    

    def get_municipality(self, id):
        read_municipality = Municipality.query.filter_by(codeMunicipality=id).first()
        if read_municipality:
            data = {
                'id': id,
                'muncipalidad': read_municipality.nameMunicipality,
                'postalCodigo': read_municipality.postalCode,
                'IdDepartamento': read_municipality.codeDepartment,
                'estadoMunicipio': read_municipality.status_mun
            }
        else:
            return None

        return data
    

    def update_municipality(self, data, usr):
        try: 
            refresh_municipality = Municipality.query.filter_by(codeMunicipality=data['id']).first()
            if refresh_municipality:            
                if data['muncipalidad']: 
                    refresh_municipality.nameMunicipality = data['muncipalidad']
                
                if data['postalCodigo']:
                    refresh_municipality.postalCode = data['postalCodigo']
                
                if data['IdDepartamento']:
                    refresh_municipality.codeDepartment = data['IdDepartamento']

                if data['estadoMunicipio']:
                    refresh_municipality.status_mun = data['estadoMunicipio']

                refresh_municipality.usr_update = usr
                refresh_municipality.tim_update = datetime.now()            
                db.session.commit()

                return refresh_municipality
            
            return constants.NOT_FOUND

        except Exception as e:
            print('---------------> ERROR update_municipality: ---------------> ', e)
            return None