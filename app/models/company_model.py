from ..database import db

class Company(db.Model):

    __tablename__ = 'company'
    __table_args__ = {'schema': 'ap_general'}

    Id_company = db.Column(db.String(15), primary_key=True)
    nameCompany = db.Column(db.String(128), nullable=False)
    address = db.Column(db.String(250), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    aditionalPhone = db.Column(db.String(15))
    representative = db.Column(db.String(250), nullable=False)
    codeNumeric = db.Column(db.String(3), db.ForeignKey('ap_general.country.codeNumeric'), nullable=False)
    codeDepartment = db.Column(db.Integer, db.ForeignKey('ap_general.departament.codeDepartment'), nullable=False)
    codeMunicipality = db.Column(db.Integer, db.ForeignKey('ap_general.municipality.codeMunicipality'), nullable=False)    

    #columnas de auditoria.
    status_com = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)