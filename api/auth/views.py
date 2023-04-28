from flask_restx import Namespace, Resource


auth_namespace = Namespace('auth', description="Namespace for authentication")



@auth_namespace.route('/signup')
class SignUp(Resource):
    def post(self):
        ''' Create a new User'''
        pass

@auth_namespace.route('/login')
class Login (Resource):
    def post (self):
        '''Generet JWT'''
        pass

