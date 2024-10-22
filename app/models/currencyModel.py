from ..database import db

class Currency(db.Model):

    __tablename__ = 'currency'
    __table_args__ = {'schema': 'ap_general'}

    codeCurrency = db.Column(db.String(3), primary_key=True)
    symbol = db.Column(db.String(2), nullable=False)
    ISO2 = db.Column(db.String(3), nullable=False)
    ISO3 = db.Column(db.String(3), nullable=False)
    nameCurrency = db.Column(db.String(128), nullable=False)
    codeNumeric = db.Column(db.String(3), db.ForeignKey('ap_general.country.codeNumeric'), nullable=False)
    
    #columnas de auditoria.
    status_cur = db.Column(db.String(1), nullable=False)
    usr_create = db.Column(db.String(20), nullable=False)
    tim_create = db.Column(db.DateTime, nullable=False)  
    usr_update = db.Column(db.String(20))
    tim_update = db.Column(db.DateTime)