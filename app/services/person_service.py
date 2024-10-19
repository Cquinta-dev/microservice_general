from app.models.personModel import Person
from app.database import db
from datetime import datetime

class PersonService:


    def create_person(self, data, usr):

        new_person = Person (
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

    
    def get_all_persons(self):

        getPersons = Person.query.all()
        if getPersons:
            data = {
                'personas': [
                    {
                        'id': p.id_person,
                        'nombres': p.name,
                        'apellidos': p.lastname,
                        'correo': p.email,
                        'estado': p.status_per
                    } for p in getPersons
                ]
            }
        else:
            return None

        return data
    

    def get_person(self, id):

        getPerson = Person.query.filter_by(id_person=id).first()
        if getPerson:
            data = {
                'id': getPerson.id_person,
                'nombres': getPerson.name,
                'apellidos': getPerson.lastname,
                'correo': getPerson.email,
                'estado': getPerson.status_per
            }
        else:
            return None

        return data
        

    def update_person(self, data, usr):
        
        person = Person.query.filter_by(id_person=data['id']).first()
        if person:            
            if data['nombres']: 
                person.name = data['nombres']
            
            if data['apellidos']:
                person.lastname = data['apellidos']
            
            if data['correo']:
                person.email = data['correo']

            if data['estado']:
                person.status_per = data['estado']

            person.usr_update = usr
            person.tim_update = datetime.now()            
            db.session.commit()

            return person
        
        return None