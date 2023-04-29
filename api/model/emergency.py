from ..utils import db
from datetime import datetime



class Emergency(db.Model):
    __tablename__="Emergency"
    id =db.Column(db.Integer, primary_key= True)
    case_id = db.Column(db.Integer, nullable= False)
    nature_of_emergency = db.Column(db.String(50), nullable= False)
    location = db.Column(db.String(50), nullable= False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)