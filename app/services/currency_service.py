from app.models.currency_model import Currency
from app.database import db
from datetime import datetime
from ..utils.constants import constants

class CurrencyService:


    def create_currency(self, data, usr):
        try:
            new_currency = Currency (
                codeCurrency = data['id'], 
                symbol = data['simboloMoneda'],
                ISO2 = data['isoDos'],
                ISO3 = data['isoTres'],
                nameCurrency = data['moneda'],
                codeNumeric = data['IdPais'],

                status_cur = 'E',
                usr_create = usr,
                tim_create = datetime.now()
            )
            
            db.session.add(new_currency)
            db.session.commit()

            return new_currency
        
        except Exception as e:
            print('---------------> ERROR create_currency: ---------------> ', e)
            return None


    def get_all_currencies(self):
        read_currencies = Currency.query.all()
        if read_currencies:
            data = {
                'monedas': [
                    {
                        'id': p.codeCurrency,
                        'simboloMoneda': p.symbol,
                        'isoDos': p.ISO2,
                        'isoTres': p.ISO3,
                        'moneda': p.nameCurrency,
                        'IdPais': p.codeNumeric,
                        'estadoMoneda': p.status_cur
                    } for p in read_currencies
                ]
            }
        else:
            return None

        return data
    

    def get_currency(self, id):
        read_currency = Currency.query.filter_by(codeCurrency=id).first()
        if read_currency:
            data = {
                'id': id,
                'simboloMoneda': read_currency.symbol,
                'isoDos': read_currency.ISO2,
                'isoTres': read_currency.ISO3,
                'moneda': read_currency.nameCurrency,
                'IdPais': read_currency.codeNumeric,
                'estadoMoneda': read_currency.status_cur
            }
        else:
            return None

        return data
    

    def update_currency(self, data, usr):
        try:
            refresh_currency = Currency.query.filter_by(codeCurrency=data['id']).first()
            if refresh_currency:            
                if data['simboloMoneda']: 
                    refresh_currency.symbol = data['simboloMoneda']
                
                if data['isoDos']:
                    refresh_currency.ISO2 = data['isoDos']
                
                if data['isoTres']:
                    refresh_currency.ISO3 = data['isoTres']

                if data['moneda']:
                    refresh_currency.nameCurrency = data['moneda']

                if data['IdPais']:
                    refresh_currency.codeNumeric = data['IdPais']
                
                if data['estadoMoneda']:
                    refresh_currency.status_cur = data['estadoMoneda']

                refresh_currency.usr_update = usr
                refresh_currency.tim_update = datetime.now()            
                db.session.commit()

                return refresh_currency
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_currency: ---------------> ', e)
            return None        