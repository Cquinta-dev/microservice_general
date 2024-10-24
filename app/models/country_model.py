from ..database import db

class Country(db.Model):

    __tablename__ = 'country'
    __table_args__ = {'schema': 'ap_general'}

    idCountry = db.Column(db.Integer, primary_key=True, autoincrement=True)
    codeCountry = db.Column(db.String(3), nullable=False)
    ISO2 = db.Column(db.String(2), nullable=False)
    ISO3 = db.Column(db.String(3), nullable=False)
    nameContry = db.Column(db.String(128), nullable=False, unique=True)
    capitalContry = db.Column(db.String(128), nullable=False)
    postalCode = db.Column(db.String(5), nullable=False)

    #columnas de auditoria.
    status = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)