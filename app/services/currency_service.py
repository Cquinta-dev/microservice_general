from ..utils.validate_registers import ValidateRegister
from ..models.currency_model import Currency
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class CurrencyService:


    def create_currency(self, data, usr):
        try:
            if ValidateRegister.currency_exists(data['moneda']):
                return f"{constants.EXIST}{data['moneda']}"
            else:                
                validate = ValidateRegister.validate_country_status(data['IdPais'])
                if validate == constants.Ok:
                    new_currency = Currency (
                        codeCurrency = data['id'], 
                        symbol = data['simboloMoneda'],
                        ISO2 = data['isoDos'],
                        ISO3 = data['isoTres'],
                        nameCurrency = data['moneda'],
                        codeCountry = data['IdPais'],

                        status_cur = constants.ENABLED,
                        usr_create = usr,
                        tim_create = datetime.now()
                    )
                    
                    db.session.add(new_currency)
                    db.session.commit()

                    return f"{constants.CREATE}Currency {data['moneda']}"
                
                else:

                    return validate
        
        except Exception as e:
            print('---------------> ERROR create_currency: ---------------> ', e)
            return None


    def get_currencies(self):
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
                        'IdPais': p.codeCountry,
                        'estadoMoneda': p.status_cur
                    } for p in read_currencies
                ]
            }
        else:
            return None

        return data
    

    def get_combo_currencies(self, id):
        read_currencies = Currency.query.filter(
                            Currency.codeCountry == id,
                            Currency.status_cur == constants.ENABLED)
        if read_currencies.count() == 0:
            return None
        
        if read_currencies:
            data = {
                'monedas': [
                    {
                        'id': p.codeCurrency,
                        'simboloMoneda': p.symbol,
                        'isoDos': p.ISO2,
                        'isoTres': p.ISO3,
                        'moneda': p.nameCurrency,
                        'IdPais': p.codeCountry,
                        'estadoMoneda': p.status_cur
                    } for p in read_currencies
                ]
            }

        return data
    

    def update_currency(self, data, usr):
        try:
            refresh_currency = Currency.query.filter_by(codeCurrency=data['id']).first()
            if refresh_currency:                
                validate = ValidateRegister.validate_country_status(data['IdPais'])
                if validate == constants.Ok:
                    if data['simboloMoneda']: 
                        refresh_currency.symbol = data['simboloMoneda']
                    
                    if data['isoDos']:
                        refresh_currency.ISO2 = data['isoDos']
                    
                    if data['isoTres']:
                        refresh_currency.ISO3 = data['isoTres']

                    if data['moneda']:
                        refresh_currency.nameCurrency = data['moneda']

                    if data['IdPais']:
                        refresh_currency.codeCountry = data['IdPais']
                    
                    if data['estadoMoneda']:
                        refresh_currency.status_cur = data['estadoMoneda']

                    refresh_currency.usr_update = usr
                    refresh_currency.tim_update = datetime.now()            
                    db.session.commit()

                    return f"{constants.UPDATE}Currency {data['moneda']}"

                else:

                    return validate  
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_currency: ---------------> ', e)
            return None        