from app.models.company_model import Company
from app.database import db
from datetime import datetime
from ..utils.constants import constants

class CompanyService:


    def create_company(self, data, usr):
        try:
            new_company = Company (
                Id_company = data['id'], 
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
        
        except Exception as e:
            print('---------------> ERROR create_company: ---------------> ', e)
            return None


    def get_all_companies(self):
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
                        'IdPais': p.codeNumeric,
                        'IdDepartamento': p.codeDepartment,
                        'IdMunicipalidad': p.codeMunicipality,
                        'estadoEmpresa': p.status_com
                    } for p in read_companies
                ]
            }
        else:
            return None

        return data
    
    
    def get_company(self, id):
        read_company = Company.query.filter_by(Id_company=id).first()
        if read_company:
            data = {
                'id': id,
                'nombreComercio': read_company.nameCompany,
                'direccionComercio': read_company.address,
                'TelefonoPbx': read_company.phone,
                'otroTelefonoPbx': read_company.aditionalPhone,
                'representanteLegal': read_company.representative,
                'IdPais': read_company.codeNumeric,
                'IdDepartamento': read_company.codeDepartment,
                'IdMunicipalidad': read_company.codeMunicipality,
                'estadoEmpresa': read_company.status_com
            }
        else:
            return None

        return data
    

    def update_company(self, data, usr):
        try:
            refresh_company = Company.query.filter_by(Id_company=data['id']).first()
            if refresh_company:            
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
                    refresh_company.codeNumeric = data['IdPais']

                if data['IdDepartamento']:
                    refresh_company.codeDepartment = data['IdDepartamento']

                if data['IdMunicipalidad']:
                    refresh_company.codeMunicipality = data['IdMunicipalidad']

                if data['estadoEmpresa']:
                    refresh_company.status_com = data['estadoEmpresa']

                refresh_company.usr_update = usr
                refresh_company.tim_update = datetime.now()            
                db.session.commit()

                return refresh_company
            
            return constants.NOT_FOUND
           
        except Exception as e:
            print('---------------> ERROR update_company: ---------------> ', e)
            return None