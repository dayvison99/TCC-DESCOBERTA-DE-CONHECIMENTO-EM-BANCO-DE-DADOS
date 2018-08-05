from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField, TextField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField


class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class CadastroUsuarioForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    cpf = StringField('cpf',validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    celular = StringField('celular',validators=[DataRequired()])
    nomeUsuario = StringField('nome de Usuario')
    senha = PasswordField ('senha',validators=[DataRequired()])
