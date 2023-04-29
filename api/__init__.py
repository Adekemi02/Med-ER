from flask import Flask 
from .auth.views import auth_namespace
from flask_restx import Api
from .config.config import config_dict
from flask_migrate import Migrate
from .utils import db
from .model.user import User
from .model.emergency import Emergency

def create_app(config = config_dict['dev']):
    app = Flask(__name__)

    app.config.from_object(config)

    db.init_app(app)

    migrate = Migrate(app, db)

    api = Api(app)

    api.add_namespace(auth_namespace, path='/auth')

    @app.shell_context_processor
    def make_shell_context():
        return {
            "db": db,
            "User": User,
            "Emergency": Emergency
        }
    
    return app