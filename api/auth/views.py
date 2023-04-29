from flask_restx import Namespace, Resource, fields
from ..model.user import User
from flask import request
from werkzeug.security import generate_password_hash, check_password_hash
from http import HTTPStatus



auth_namespace = Namespace('auth', description="Namespace for authentication")

signup_model = auth_namespace.model(
    'SignUp', {
        'first_name': fields.String(required=True, description='First Name'),
        'last_name': fields.String(required=True, description='Last Name'),
        'other_names': fields.String(description='Other Names'),
        'password': fields.String(required=True, description='Password'),
        'email': fields.String(required=True, description='Email'),
        'phone_no': fields.Integer(required=True, description='Phone Number'),
        'blood_group': fields.String(required=True, description='Blood Group'),
        'gender': fields.String(required=True, description='Gender'),
        'genotype': fields.String(required=True, description='Genotype'),
        'age': fields.Integer(required=True, description='Age'),
    }
)

login_model = auth_namespace.model(
    'Login', {
        'email': fields.String(required=True, description='Email'),
        'password': fields.String(required=True, description='Password'),
    }
)

@auth_namespace.route('/signup')
class SignUp(Resource):
    @auth_namespace.expect(signup_model)
    @auth_namespace.marshal_with(signup_model)
    @auth_namespace.doc(description="User sign up")

    def post(self):
        ''' Create a new User'''

        data = request.get_json()

        user = User(
            first_name = data.get('first_name'),
            last_name = data.get('last_name'),
            other_names = data.get('other_names'),
            password_hash = generate_password_hash(data.get('password')),
            email = data.get('email'),
            phone_no = data.get('phone_no'),
            blood_group = data.get('blood_group'),
            gender = data.get('gender'),
            genotype = data.get('genotype'),
            age = data.get('age')
        )

        user.save()

        return user, HTTPStatus.CREATED

@auth_namespace.route('/login')
class Login (Resource):
    def post (self):
        '''Generet JWT'''
        pass

