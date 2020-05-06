from flask import Blueprint

user_api_blueprint = Blueprint('user_api_blueprint', __name__,  template_folder='templates', static_folder='static')
