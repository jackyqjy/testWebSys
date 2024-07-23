from models.user import UserModel
from .baseform import BaseForm
from wtforms import Form, StringField, ValidationError

class loginForm(BaseForm):
    remember = True#BooleanField()