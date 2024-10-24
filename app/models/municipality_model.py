from ..database import db

class Municipality(db.Model):

    __tablename__ = 'municipality'
    __table_args__ = {'schema': 'ap_general'}
    
    idMunicipality = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nameMunicipality = db.Column(db.String(128), nullable=False, unique=True)
    postalCode = db.Column(db.String(10))
    idDepartment = db.Column(db.Integer, db.ForeignKey('ap_general.departament.idDepartment'), nullable=False)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)