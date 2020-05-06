from flask import Blueprint, Flask
from flask_login import LoginManager
from flask_bootstrap import Bootstrap
from .frontend import frontend_blueprint

app = Flask(__name__)

# Helps limit views to authenticated users
login_manager = LoginManager(app)
login_manager.init_app(app)
login_manager.login_view = 'main.login'

bootstrap = Bootstrap(app)

app.config.update(dict(
    SECRET_KEY="",
    WTF_CSRF_SECRET_KEY="",
    PRODUCT_SERVICE='HTTP://localhost:8080'
))

app.register_blueprint(frontend_blueprint)

app.run(debug=True, host='0.0.0.0')