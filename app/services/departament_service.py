from app.models.departament_Model import Departament
from app.database import db
from datetime import datetime

class DepartamentService:


    def create_departament(self, data, usr):

        new_departament = Departament (
            nameDepartament = data['departamento'],
            headboardDepartament = data['cabecera'],
            postalCode = data['postalCodigo'],
            codeNumeric = data['idPais'],

            status_dep = 'E',
            usr_create = usr,
            tim_create = datetime.now()
        )
        
        db.session.add(new_departament)
        db.session.commit()

        return new_departament