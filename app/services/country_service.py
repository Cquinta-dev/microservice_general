from app.models.country_model import Country
from app.database import db
from datetime import datetime
from ..utils.constants import constants

class CountryService:


    def create_country(self, data, usr):
        try:
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
               
        except Exception as e:
            print('---------------> ERROR create_country: ---------------> ', e)
            return None


    def get_all_countries(self):
        read_countries = Country.query.all()
        if read_countries:
            data = {
                'paises': [
                    {
                        'id': p.codeNumeric,
                        'codigoDos': p.ISO2,
                        'CodigoTres': p.ISO3,
                        'pais': p.nameContry,
                        'capital': p.capitalContry,
                        'postalCodigo': p.postalCode,
                        'estadoPais': p.status_cou
                    } for p in read_countries
                ]
            }
        else:
            return None

        return data    


    def get_country(self, id):
        read_country = Country.query.filter_by(codeNumeric=id).first()
        if read_country:
            data = {
                'id': id,
                'codigoDos': read_country.ISO2,
                'CodigoTres': read_country.ISO3,
                'pais': read_country.nameContry,
                'capital': read_country.capitalContry,
                'postalCodigo': read_country.postalCode,
                'estadoPais': read_country.status_cou
            }
        else:
            return None

        return data    


    def update_country(self, data, usr):
        try:        
            refresh_country = Country.query.filter_by(codeNumeric=data['id']).first()
            if refresh_country:            
                if data['codigoDos']: 
                    refresh_country.ISO2 = data['codigoDos']
                
                if data['CodigoTres']:
                    refresh_country.ISO3 = data['CodigoTres']
                
                if data['pais']:
                    refresh_country.nameContry = data['pais']

                if data['capital']:
                    refresh_country.capitalContry = data['capital']

                if data['postalCodigo']:
                    refresh_country.postalCode = data['postalCodigo']

                if data['estadoPais']:
                    refresh_country.status_cou = data['estadoPais']

                refresh_country.usr_update = usr
                refresh_country.tim_update = datetime.now()            
                db.session.commit()

                return refresh_country
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_country: ---------------> ', e)
            return None