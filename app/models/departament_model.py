from ..database import db

class Departament(db.Model):

    __tablename__ = 'departament'
    __table_args__ = {'schema': 'ap_general'}

    idDepartment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameDepartament = db.Column(db.String(128), nullable=False, unique=True)
    headboardDepartament = db.Column(db.String(128), nullable=False)
    postalCode = db.Column(db.String(10))
    idCountry = db.Column(db.Integer, db.ForeignKey('ap_general.country.idCountry'), nullable=False)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)