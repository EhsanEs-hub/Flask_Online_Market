from flask import Blueprint

frontend_blueprint = Blueprint('frontend_blueprint', __name__,  template_folder='templates', static_folder='static')
