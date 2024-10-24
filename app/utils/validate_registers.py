from sqlalchemy import exists
from ..models.municipalityModel import Municipality
from ..models.departamentModel import Departament
from ..models.currency_model import Currency
from ..models.countryModel import Country
from ..utils.constants import constants
from ..database import db 

class ValidateRegisters:


    @staticmethod
    def country_exists(code_country):
        return db.session.query(exists().where(Country.codeCountry == code_country)).scalar()


    @staticmethod
    def validate_country(id):
        search_country = Country.query.filter_by(codeCountry=id).first()
        if search_country: 
            if search_country.status_cou == constants.ENABLED:            
                return constants.Ok
            
            return f"Country {search_country.nameContry} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Country {id}"


    @staticmethod
    def departament_exists(nameDepartament):
        return db.session.query(exists().where(Departament.nameDepartament == nameDepartament)).scalar()
    

    @staticmethod
    def validate_departament(id):
        search_departament = Departament.query.filter_by(codeDepartment=id).first()
        if search_departament: 
            if search_departament.status_dep == constants.ENABLED:            
                return constants.Ok
            
            return f"Departament {search_departament.nameDepartament} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Departament {id}"


    @staticmethod
    def currency_exists(nameCurrency):
        return db.session.query(exists().where(Currency.nameCurrency == nameCurrency)).scalar()
    

    @staticmethod
    def municipality_exists(nameMunicipality):
        return db.session.query(exists().where(Municipality.nameMunicipality == nameMunicipality)).scalar()