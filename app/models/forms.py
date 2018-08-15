from flask_wtf import FlaskForm
from wtforms import Form,validators
from wtforms import StringField, PasswordField, BooleanField, TextField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("password", validators=[DataRequired()])
    remember_me = BooleanField("remember_me")
    tipo = StringField("tipo")

class CadastroUsuarioForm(FlaskForm):
    nome = StringField('nome', validators=[DataRequired()])
    cpf = StringField('cpf',validators=[DataRequired()])
    email = EmailField('email',validators=[DataRequired()])
    celular = TextField('celular',validators=[DataRequired()])
    nomeUsuario = StringField('nome de Usuario',validators=[DataRequired()])
    senha = PasswordField ('senha',[
        validators.DataRequired(),
        validators.EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repita a senha',validators=[DataRequired()])
    tipo = StringField("tipo",validators=[DataRequired()])
