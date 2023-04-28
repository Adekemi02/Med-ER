from ..utils import db
from user import User



class Emergency(db.Model):
    __tablename__="EmergencyRecord"
    id =db.Column(db.Integer(), primary_key= True)
    case_id = db.Column()