from app.models.person_model import Person
from app.database import db
from datetime import datetime
from ..utils.constants import constants

class PersonService:


    def create_person(self, data, usr):
        try:
            new_person = Person (
                Id_company = data['idComercio'],
                id_person = data['id'], 
                name = data['nombres'],
                lastname = data['apellidos'],
                email = data['correo'],
                
                status_per = 'E',
                usr_create = usr,
                tim_create = datetime.now()
            )
            
            db.session.add(new_person)
            db.session.commit()

            return new_person
        except Exception as e:
            print('---------------> ERROR create_person: ---------------> ', e)
            return None
        
    
    def get_all_persons(self):
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
    

    def get_person(self, id):

        read_person = Person.query.filter_by(id_person=id).first()
        if read_person:
            data = {
                'id': id,
                'nombres': read_person.name,
                'apellidos': read_person.lastname,
                'correo': read_person.email,
                'estadoPersona': read_person.status_per
            }
        else:
            return None

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

                return refresh_person
        
            return constants.NOT_FOUND

        except Exception as e:
            print('---------------> ERROR update_person: ---------------> ', e)
            return None