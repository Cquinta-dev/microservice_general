from ..database import db

class Person(db.Model):

    __tablename__ = 'persons'  # Nombre de la tabla
    __table_args__ = {'schema': 'ap_general'}  # Especifica el esquema

    id_person = db.Column(db.String(50), primary_key=True)    
    name = db.Column(db.String(150), nullable=False)
    lastname = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)

    #columnas de auditoria.
    status_per = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)