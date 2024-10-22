from app.models.municipality_Model import Municipality
from app.database import db
from datetime import datetime

class MunicipalityService:


    def create_municipality(self, data, usr):

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