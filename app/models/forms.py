from flask_wtf import FlaskForm
from wtforms import Form
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")

class CadastroUsuarioForm(FlaskForm):
    nome = StringField('Nome',validators=[DataRequired()])
    cpf = StringField('Cpf',validators=[DataRequired()])
    email = EmailField('Email',validators=[DataRequired()])
    celular = StringField('Celular',validators=[DataRequired()])
    nomeUsuario = StringField('Nome de Usuario')
    senha = PasswordField ('Senha',validators=[DataRequired()])
