from app.models.country_Model import Country
from app.database import db
from datetime import datetime

class CountryService:


    def create_country(self, data, usr):

        new_country = Country (
            codeNumeric = data['id'],
            ISO2 = data['codigoDos'], 
            ISO3 = data['CodigoTres'], 
            nameContry = data['pais'],
            capitalContry = data['capital'],
            postalCode = data['postalCodigo'],

            status_cou = 'E',
            usr_create = usr,
            tim_create = datetime.now()
        )
        
        db.session.add(new_country)
        db.session.commit()

        return new_country