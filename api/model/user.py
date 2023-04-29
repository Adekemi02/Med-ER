from ..utils import db
from enum import Enum


class BloodGroup(Enum):
    A_POSITIVE = 'A+'
    A_NEGATIVE = 'A-'
    B_POSITIVE = 'B+'
    B_NEGATIVE = 'B-'
    AB_POSITIVE = 'AB+'
    AB_NEGATIVE = 'AB-'
    O_POSITIVE = 'O+'
    O_NEGATIVE = 'O-'

class Genotype(Enum):
    AA ='AA'
    AS = 'AS'
    SS = 'SS'
    AC = 'AC'
    CC = 'CC'


class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(50), nullable= False)
    last_name = db.Column(db.String(50), nullable= False)
    other_names= db.Column(db.String(60), nullable = True)
    email= db.Column(db.String(40),unique= True, nullable=False)
    password_hash = db.Column(db.Text, nullable = False)
    phone_no = db.Column(db.Integer,nullable= False)
    blood_group= db.Column(db.Enum(BloodGroup), nullable = False)
    genotype = db.Column(db.Enum(Genotype), nullable = False)
    age =db.Column(db.Integer, nullable = False)
    gender = db.Column(db.String(15), nullable = False)
    address= db.Column(db.String(250))
    next_of_kin_name= db.Column(db.String(50))
    next_of_kin_relationship= db.Column(db.String(50))
    next_of_kin_address = db.Column(db.String(250))
    emergency = db.relationship('Emergency', backref='user', lazy=True)
    

    def __repr__(self):
        return f"User{self.id}"
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete()
        db.session.commit()



