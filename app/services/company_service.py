from ..utils.validate_registers import ValidateRegister
from ..models.company_model import Company
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class CompanyService:


    def create_company(self, data, usr):
        try:
            if ValidateRegister.company_exists(data['identificacion']):
                return f"{constants.EXIST}{data['nombreComercio']}"
            else:
                validate = ValidateRegister.validate_country_status(data['codPais'])
                if validate == constants.Ok:
                    validate = ValidateRegister.validate_departament_status(data['codDepartamento'])
                    if validate == constants.Ok:
                        validate = ValidateRegister.validate_municipality_status(data['codMunicipalidad'])
                        if validate == constants.Ok:
                            new_company = Company (
                                codeCompany = data['identificacion'], 
                                nameCompany = data['nombreComercio'],
                                phone = data['telefonoPbx'],                                                            
                                aditionalPhone = data['otroTelefonoPbx'],
                                representative = data['representanteLegal'],
                                address = data['direccionComercio'],    
                                idCountry = data['codPais'],
                                idDepartment = data['codDepartamento'],
                                idMunicipality = data['codMunicipalidad'],

                                status = constants.ENABLED,
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
                        'id': p.idCompany,
                        'identificacion': p.codeCompany,
                        'nombreComercio': p.nameCompany,
                        'direccionComercio': p.address,
                        'telefonoPbx': p.phone,
                        'otroTelefonoPbx': p.aditionalPhone,
                        'representanteLegal': p.representative,
                        'codPais': p.idCountry,
                        'codDepartamento': p.idDepartment,
                        'codMunicipalidad': p.idMunicipality,
                        'estadoEmpresa': p.status
                    } for p in read_companies
                ]
            }
        else:
            return None

        return data
    
    
    def get_combo_companies(self):
        read_companies = Company.query.filter(Company.status == constants.ENABLED)
        if read_companies.count() == 0:
            return None
        
        if read_companies:
            data = {
                'empresas': [
                    {
                        'id': p.idCompany,
                        'nombreComercio': p.nameCompany
                    } for p in read_companies
                ]
            }

        return data
    

    def update_company(self, data, usr):
        try:            
            refresh_company = Company.query.filter_by(idCompany=data['id']).first()
            if refresh_company:     
                validate = ValidateRegister.validate_country_status(data['codPais'])
                if validate == constants.Ok:
                    validate = ValidateRegister.validate_departament_status(data['codDepartamento'])
                    if validate == constants.Ok:
                        validate = ValidateRegister.validate_municipality_status(data['codMunicipalidad'])
                        if validate == constants.Ok:      
                            if data['identificacion']: 
                                refresh_company.codeCompany = data['identificacion']

                            if data['nombreComercio']: 
                                refresh_company.nameCompany = data['nombreComercio']                                                    
                            
                            if data['telefonoPbx']:
                                refresh_company.phone = data['telefonoPbx']

                            if data['otroTelefonoPbx']:
                                refresh_company.aditionalPhone = data['otroTelefonoPbx']

                            if data['representanteLegal']:
                                refresh_company.representative = data['representanteLegal']

                            if data['direccionComercio']:
                                refresh_company.address = data['direccionComercio']

                            if data['codPais']:
                                refresh_company.idCountry = data['codPais']

                            if data['codDepartamento']:
                                refresh_company.idDepartment = data['codDepartamento']

                            if data['codMunicipalidad']:
                                refresh_company.idMunicipality = data['codMunicipalidad']

                            if data['estadoEmpresa']:
                                refresh_company.status = data['estadoEmpresa']

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