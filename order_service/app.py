from flask import Flask, Blueprint
from .order_api import order_api_blueprint
import models

app = Flask(__name__)

app.config.update(dict(
    SECRET_KEY="",
    WTF_CSRF_SECRET_KEY="",
    SQLALCHEMY_DATABASE_URI ='mysql+mysqlconnector://root:@localhost/order',
))

models.init_app(app)
models.create_tables(app)

app.register_blueprint(order_api_blueprint)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


