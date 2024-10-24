from ..utils.validate_registers import ValidateRegister
from ..models.person_model import Person
from ..utils.constants import constants
from ..database import db
from datetime import datetime


class PersonService:


    def create_person(self, data, usr):
        try:
            if ValidateRegister.person_exists(data['idComercio'], data['id']):
                return f"{constants.EXIST}{data['nombres'], data['apellidos']}"
            else:
                validate = ValidateRegister.validate_company_status(data['idComercio'])
                if validate == constants.Ok:                
                    new_person = Person (
                        Id_company = data['idComercio'],
                        id_person = data['id'], 
                        name = data['nombres'],
                        lastname = data['apellidos'],
                        email = data['correo'],
                        
                        status_per = constants.ENABLED,
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
                        'id': p.id_person,
                        'nombres': p.name,
                        'apellidos': p.lastname,
                        'correo': p.email,
                        'estadoPersona': p.status_per
                    } for p in read_persons
                ]
            }
        else:
            return None

        return data
    

    def get_combo_persons(self, id):
        read_persons = Person.query.filter(
                        Person.Id_company == id,
                        Person.status_per == constants.ENABLED)
        if read_persons.count() == 0:
            return None

        if read_persons:
            data = {
                'personas': [
                    {
                        'id': p.id_person,
                        'nombres': p.name,
                        'apellidos': p.lastname                        
                    } for p in read_persons
                ]
            }    

        return data
        

    def update_person(self, data, usr):
        try:        
            refresh_person = Person.query.filter_by(id_person=data['id']).first()
            if refresh_person:   
                if data['nombres']: 
                    refresh_person.name = data['nombres']
                
                if data['apellidos']:
                    refresh_person.lastname = data['apellidos']
                
                if data['correo']:
                    refresh_person.email = data['correo']

                if data['estadoPersona']:
                    refresh_person.status_per = data['estadoPersona']

                refresh_person.usr_update = usr
                refresh_person.tim_update = datetime.now()            
                db.session.commit()

                return f"{constants.UPDATE}Person {data['nombres'], data['apellidos']}"
        
            return constants.NOT_FOUND

        except Exception as e:
            print('---------------> ERROR update_person: ---------------> ', e)
            return None