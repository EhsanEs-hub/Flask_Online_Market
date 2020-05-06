from flask import Flask, Blueprint, g  # Global
from flask_login import LoginManager, user_loaded_from_header
from flask.sessions import SecureCookieSessionInterface
from .user_api import user_api_blueprint
import models

app = Flask(__name__)

login_manager = LoginManager(app)
login_manager.init_app(app)

app.config.update(dict(
    SECRET_KEY="",
    SQLALCHEMY_DATABASE_URI='mysql+mysqlconnector://root:@localhost/user',
))

models.init_app(app)
models.create_tables(app)

app.register_blueprint(user_api_blueprint)

@login_manager.user_loader
def load_user(user_id):
    return models.user.query.filter_by(id=user_id).first()

@login_manager.request_loader
def load_user_from_request(request):

    # Try to login using Basic Auth
    api_key = request.headers.get('Authorization')

    if api_key:
        api_key = api_key.replace('Basic', '', 1)
        user = models.user.query.filter_by(api_key=api_key).first()
        if user:
            return user
    return None

class CustomSessionInterface(SecureCookieSessionInterface):
    """ prevent creating session from API requests."""
    def save_session(self, *args, **kwargs):
        if g.get('login_via_header'):
            return
        return super(CustomSessionInterface, self).save_session(*args, **kwargs)
app.session_interface = CustomSessionInterface()

# Using g object to store the profile owner available in Jinja2 template context
@user_loaded_from_header.connect
def user_loaded_from_header(self, user=None):
    g.login_via_header = True

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

