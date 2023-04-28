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


class User(db.model):
    __tablename__ = "user"
    id = db.Column(db.Integer(), primary_key = True)
    first_name = db.Column(db.String(50), nullable= False)
    last_name = db.Column(db.String(50), nullable= False)
    other_names= db.Column(db.String(60), nullable = True)
    email= db.Column(db.String(40),unique= True, nullable=False)
    phone_no = db.Column(db.Integer(11),nullable= False)
    blood_group= db.Column(db.Enum(BloodGroup), nullable = False)
    genotype = db.Column(db.Enum(Genotype), nullable = False)
    age =db.Column(db.Integer(3), nullable = False)
    gender = db.Column(db.String(), nullable = False)
    address= db.Column(db.String())
    next_of_kin_name= db.Column(db.String())
    next_of_kin_relationship= db.Column(db.String())
    next_of_kin_address = db.Column(db.String())
    





    def __repr__(self):
        return f"User{self.id}"
    



