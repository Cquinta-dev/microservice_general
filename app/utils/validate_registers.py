from sqlalchemy import exists
from ..models.municipality_model import Municipality
from ..models.departament_model import Departament
from ..models.currency_model import Currency
from ..models.company_model import Company
from ..models.country_model import Country
from ..models.person_model import Person
from ..database import db 
from .constants import constants


class ValidateRegister:


    def country_exists(code_country):
        return db.session.query(exists().where(Country.codeCountry == code_country)).scalar()


    def validate_country_status(id):
        search_country = Country.query.filter_by(codeCountry=id).first()
        if search_country: 
            if search_country.status_cou == constants.ENABLED:            
                return constants.Ok
            
            return f"Country {search_country.nameContry} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Country {id}"


    def departament_exists(nameDepartament):
        return db.session.query(exists().where(Departament.nameDepartament == nameDepartament)).scalar()
    

    def validate_departament_status(id):
        search_departament = Departament.query.filter_by(codeDepartment=id).first()
        if search_departament: 
            if search_departament.status_dep == constants.ENABLED:            
                return constants.Ok
            
            return f"Departament {search_departament.nameDepartament} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Departament {id}"

    
    def municipality_exists(nameMunicipality):
        return db.session.query(exists().where(Municipality.nameMunicipality == nameMunicipality)).scalar()
    

    def validate_municipality_status(id):
        search_municipality = Municipality.query.filter_by(codeMunicipality=id).first()
        if search_municipality: 
            if search_municipality.status_mun == constants.ENABLED:            
                return constants.Ok
            
            return f"Municipality {search_municipality.nameMunicipality} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Municipality {id}"


    def company_exists(Id_company):
        return db.session.query(exists().where(Company.Id_company == Id_company)).scalar()
    

    def validate_company_status(Id):
        search_company = Company.query.filter_by(Id_company=Id).first()
        if search_company: 
            if search_company.status_com == constants.ENABLED:            
                return constants.Ok
            
            return f"Company {search_company.nameCompany} {constants.MESSAGE_DISABLED}" 

        return f"{constants.NOT_EXIST} Company {id}"


    def currency_exists(nameCurrency):
        return db.session.query(exists().where(Currency.nameCurrency == nameCurrency)).scalar()
    

    def person_exists(idPeson, idCompany):
        return db.session.query(exists().where(Person.id_person == idPeson, Person.Id_company == idCompany)).scalar()