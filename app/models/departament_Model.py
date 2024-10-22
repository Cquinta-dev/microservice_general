from ..database import db

class Departament(db.Model):

    __tablename__ = 'departament'
    __table_args__ = {'schema': 'ap_general'}

    codeDepartment = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameDepartament = db.Column(db.String(128), nullable=False)
    headboardDepartament = db.Column(db.String(128), nullable=False)
    postalCode = db.Column(db.String(10))
    codeNumeric = db.Column(db.String(3), db.ForeignKey('ap_general.country.codeNumeric'), nullable=False)

    #columnas de auditoria.
    status_dep = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)