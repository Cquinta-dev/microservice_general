from ..utils.validate_registers import ValidateRegister
from ..models.person_model import Person
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class PersonService:


    def create_person(self, data, usr):
        try:
            if ValidateRegister.person_exists(data['codComercio'], data['identificacion']):
                return f"{constants.EXIST}{data['nombres'], data['apellidos']}"
            else:
                validate = ValidateRegister.validate_company_status(data['codComercio'])
                if validate == constants.Ok:                
                    new_person = Person (                    
                        idCompany = data['codComercio'],
                        codePerson = data['identificacion'], 
                        name = data['nombres'],
                        lastname = data['apellidos'],
                        email = data['correo'],
                        
                        status = constants.ENABLED,
                        usr_create = usr,
                        tim_create = datetime.now()
                    )
                    
                    db.session.add(new_person)
                    db.session.commit()

                    return f"{constants.CREATE}Person {data['nombres'], data['apellidos']}"
                
                else:

                    return validate
            
        except Exception as e:
            print('---------------> ERROR create_person: ---------------> ', e)
            return None
        
    
    def get_persons(self):
        read_persons = Person.query.all()
        if read_persons:
            data = {
                'personas': [
                    {
                        'id': p.idPerson,
                        'identificacion': p.codePerson,
                        'nombres': p.name,
                        'apellidos': p.lastname,
                        'correo': p.email,
                        'codComercio': p.idCompany,
                        'estadoPersona': p.status
                    } for p in read_persons
                ]
            }
        else:
            return None

        return data
    

    def get_combo_persons(self, id):
        read_persons = Person.query.filter(
                        Person.idCompany == id,
                        Person.status == constants.ENABLED)
        if read_persons.count() == 0:
            return None

        if read_persons:
            data = {
                'personas': [
                    {
                        'id': p.idPerson,
                        'nombres': p.name,
                        'apellidos': p.lastname                        
                    } for p in read_persons
                ]
            }    

        return data
        

    def update_person(self, data, usr):
        try:        
            refresh_person = Person.query.filter_by(idPerson=data['id']).first()
            if refresh_person:   
                if data['identificacion']: 
                    refresh_person.codePerson = data['identificacion']

                if data['nombres']: 
                    refresh_person.name = data['nombres']
                
                if data['apellidos']:
                    refresh_person.lastname = data['apellidos']
                
                if data['correo']:
                    refresh_person.email = data['correo']
                
                if data['estadoPersona']:
                    refresh_person.status = data['estadoPersona']

                if data['codComercio']:
                    refresh_person.idCompany = data['codComercio']

                refresh_person.usr_update = usr
                refresh_person.tim_update = datetime.now()            
                db.session.commit()

                return f"{constants.UPDATE}Person {data['nombres'], data['apellidos']}"
        
            return constants.NOT_FOUND

        except Exception as e:
            print('---------------> ERROR update_person: ---------------> ', e)
            return None