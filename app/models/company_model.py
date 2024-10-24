from ..database import db

class Company(db.Model):

    __tablename__ = 'company'
    __table_args__ = {'schema': 'ap_general'}

    idCompany = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codeCompany = db.Column(db.String(15), nullable=False, unique=True)
    nameCompany = db.Column(db.String(128), nullable=False, unique=True)    
    phone = db.Column(db.String(15), nullable=False)
    aditionalPhone = db.Column(db.String(15))
    representative = db.Column(db.String(250), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    idCountry = db.Column(db.Integer, db.ForeignKey('ap_general.country.idCountry'), nullable=False)
    idDepartment = db.Column(db.Integer, db.ForeignKey('ap_general.departament.idDepartment'), nullable=False)
    idMunicipality = db.Column(db.Integer, db.ForeignKey('ap_general.municipality.idMunicipality'), nullable=False)    

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)