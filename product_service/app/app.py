from flask import Flask, Blueprint
from .product_api import product_api_blueprint
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="",
    WTF_CSRF_SECRET_KEY="",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:@localhost/product',
))

models.init_app(app)
models.create_tables(app)

app.register_blueprint(product_api_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

