from flask import Blueprint

product_api_blueprint = Blueprint('product_api_blueprint', __name__,  template_folder='templates', static_folder='static')
