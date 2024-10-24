from ..utils.validate_registers import ValidateRegisters
from ..models.countryModel import Country
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class CountryService:


    def create_country(self, data, usr):
        try:
            if ValidateRegisters.country_exists(data['id']):
                return f"{constants.EXIST}{data['pais']}"
            else:
                new_country = Country (
                    codeCountry = data['id'],
                    ISO2 = data['codigoDos'], 
                    ISO3 = data['CodigoTres'], 
                    nameContry = data['pais'],
                    capitalContry = data['capital'],
                    postalCode = data['postalCodigo'],

                    status_cou = constants.ENABLED,
                    usr_create = usr,
                    tim_create = datetime.now()
                )
                
                db.session.add(new_country)
                db.session.commit()

                return f"{constants.CREATE}Country {data['pais']}"
               
        except Exception as e:
            print('---------------> ERROR create_country: ---------------> ', e)
            return None


    def get_countries(self):
        read_countries = Country.query.all()
        if read_countries:
            data = {
                'paises': [
                    {
                        'id': p.codeCountry,
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


    def get_combo_countries(self):
        read_countries = Country.query.filter(Country.status_cou == constants.ENABLED)
        if read_countries:
            data = {
                'paises': [
                    {
                        'id': p.codeCountry,
                        'pais': p.nameContry                        
                    } for p in read_countries
                ]
            }
        else:
            
            return None

        return data    


    def update_country(self, data, usr):
        try:        
            refresh_country = Country.query.filter_by(codeCountry=data['id']).first()
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

                return f"{constants.UPDATE}Country {data['pais']}"
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_country: ---------------> ', e)
            return None