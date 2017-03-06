from flask_wtf import Form
from wtforms import PasswordField, StringField, HiddenField
from wtforms.validators import Email, DataRequired


class LoginForm(Form):
    email = StringField('E-mail', [Email("Incorrect E-mail Type"), DataRequired("E-Mail Not Be Empty")])
    password = PasswordField('Password', [DataRequired("Password Not Be Empty")])