from app.models.companyModel import Company
from app.database import db
from datetime import datetime

class CompanyService:


    def create_company(self, data, usr):

        new_company = Company (
            Id_company = data['nitComercio'], 
            nameCompany = data['nombreComercio'],
            address = data['direccionComercio'],
            phone = data['TelefonoPbx'],
            aditionalPhone = data['otroTelefonoPbx'],
            representative = data['representanteLegal'],
            codeNumeric = data['IdPais'],
            codeDepartment = data['IdDepartamento'],
            codeMunicipality = data['IdMunicipalidad'],

            status_com = 'E',
            usr_create = usr,
            tim_create = datetime.now()
        )
        
        db.session.add(new_company)
        db.session.commit()

        return new_company