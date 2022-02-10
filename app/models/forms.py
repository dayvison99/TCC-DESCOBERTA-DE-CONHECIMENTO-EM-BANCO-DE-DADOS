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
    id
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

class DisciForm(FlaskForm):
        nome = StringField('nome', validators=[DataRequired()])
        periodo = StringField('periodo', validators=[DataRequired()])
        nomeData = StringField('nomeData', validators=[DataRequired()])
        equibsi = StringField('equibsi', validators=[DataRequired()])

class SituacaoDisciplinaForm(FlaskForm):
        disciplina = StringField('disciplina', validators=[DataRequired()])
        situacaoDisciplina = StringField('situacaoDisciplina', validators=[DataRequired()])
        periodo = StringField('periodo', validators=[DataRequired()])
        data = StringField('data', validators=[DataRequired()])

class AlunosForm(FlaskForm):
        nome = StringField('nome', validators=[DataRequired()])
        cpf = StringField('cpf', validators=[DataRequired()])
        resultado = StringField ('resultado')
        media = StringField ('media')
        curso = StringField('curso', validators=[DataRequired()])

class Disciplinas_AlunosForm(FlaskForm):
        id_disciplinas = StringField('id_disciplinas', validators=[DataRequired()])
        id_alunos = StringField('id_alunos', validators=[DataRequired()])
        resultado = StringField ('resultado')
        nomeDisciplina = StringField('nomeDisciplina', validators=[DataRequired()])
        status =  StringField('status')
