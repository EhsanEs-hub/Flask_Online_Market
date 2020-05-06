from flask import Blueprint

order_api_blueprint = Blueprint('order_api_blueprint', __name__,  template_folder='templates', static_folder='static')
