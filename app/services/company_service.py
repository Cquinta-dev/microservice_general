from ..utils.validate_registers import ValidateRegister
from ..models.company_model import Company
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class CompanyService:


    def create_company(self, data, usr):
        try:
            if ValidateRegister.company_exists(data['id']):
                return f"{constants.EXIST}{data['nombreComercio']}"
            else:
                validate = ValidateRegister.validate_country_status(data['IdPais'])
                if validate == constants.Ok:
                    validate = ValidateRegister.validate_departament_status(data['IdDepartamento'])
                    if validate == constants.Ok:
                        validate = ValidateRegister.validate_municipality_status(data['IdMunicipalidad'])
                        if validate == constants.Ok:
                            new_company = Company (
                                Id_company = data['id'], 
                                nameCompany = data['nombreComercio'],
                                address = data['direccionComercio'],
                                phone = data['TelefonoPbx'],
                                aditionalPhone = data['otroTelefonoPbx'],
                                representative = data['representanteLegal'],
                                codeCountry = data['IdPais'],
                                codeDepartment = data['IdDepartamento'],
                                codeMunicipality = data['IdMunicipalidad'],

                                status_com = constants.ENABLED,
                                usr_create = usr,
                                tim_create = datetime.now()
                            )
                            
                            db.session.add(new_company)
                            db.session.commit()

                            return f"{constants.CREATE}Company {data['nombreComercio']}"
                        
                        else:
                            return validate  
                    else:
                        return validate      
                else:
                    return validate  
        
        except Exception as e:
            print('---------------> ERROR create_company: ---------------> ', e)
            return None


    def get_companies(self):
        read_companies = Company.query.all()
        if read_companies:
            data = {
                'empresas': [
                    {
                        'id': p.Id_company,
                        'nombreComercio': p.nameCompany,
                        'direccionComercio': p.address,
                        'TelefonoPbx': p.phone,
                        'otroTelefonoPbx': p.aditionalPhone,
                        'representanteLegal': p.representative,
                        'IdPais': p.codeCountry,
                        'IdDepartamento': p.codeDepartment,
                        'IdMunicipalidad': p.codeMunicipality,
                        'estadoEmpresa': p.status_com
                    } for p in read_companies
                ]
            }
        else:
            return None

        return data
    
    
    def get_combo_companies(self):
        read_companies = Company.query.filter(Company.status_com == constants.ENABLED)
        if read_companies.count() == 0:
            return None
        
        if read_companies:
            data = {
                'empresas': [
                    {
                        'id': p.Id_company,
                        'nombreComercio': p.nameCompany
                    } for p in read_companies
                ]
            }

        return data
    

    def update_company(self, data, usr):
        try:            
            refresh_company = Company.query.filter_by(Id_company=data['id']).first()
            if refresh_company:     
                validate = ValidateRegister.validate_country_status(data['IdPais'])
                if validate == constants.Ok:
                    validate = ValidateRegister.validate_departament_status(data['IdDepartamento'])
                    if validate == constants.Ok:
                        validate = ValidateRegister.validate_municipality_status(data['IdMunicipalidad'])
                        if validate == constants.Ok:       
                            if data['nombreComercio']: 
                                refresh_company.nameCompany = data['nombreComercio']
                            
                            if data['direccionComercio']:
                                refresh_company.address = data['direccionComercio']
                            
                            if data['TelefonoPbx']:
                                refresh_company.phone = data['TelefonoPbx']

                            if data['otroTelefonoPbx']:
                                refresh_company.aditionalPhone = data['otroTelefonoPbx']

                            if data['representanteLegal']:
                                refresh_company.representative = data['representanteLegal']

                            if data['IdPais']:
                                refresh_company.codeCountry = data['IdPais']

                            if data['IdDepartamento']:
                                refresh_company.codeDepartment = data['IdDepartamento']

                            if data['IdMunicipalidad']:
                                refresh_company.codeMunicipality = data['IdMunicipalidad']

                            if data['estadoEmpresa']:
                                refresh_company.status_com = data['estadoEmpresa']

                            refresh_company.usr_update = usr
                            refresh_company.tim_update = datetime.now()            
                            db.session.commit()

                            return f"{constants.UPDATE}Company {data['nombreComercio']}"

                        else:
                            return validate  
                    else:
                        return validate      
                else:
                    return validate 
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_company: ---------------> ', e)
            return None