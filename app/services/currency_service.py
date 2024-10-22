from app.models.currencyModel import Currency
from app.database import db
from datetime import datetime

class CurrencyService:


    def create_currency(self, data, usr):

        new_currency = Currency (
            codeCurrency = data['id'], 
            symbol = data['simboloMoneda'],
            ISO2 = data['iso'],
            ISO3 = data['iso_3'],
            nameCurrency = data['moneda'],
            codeNumeric = data['IdPais'],

            status_cur = 'E',
            usr_create = usr,
            tim_create = datetime.now()
        )
        
        db.session.add(new_currency)
        db.session.commit()

        return new_currency