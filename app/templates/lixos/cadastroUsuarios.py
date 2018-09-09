form wtforms import Form
form wtforms import StringField, TextFiel
form wtforms.fields.html5 import EmailField

class CommentForm(Form):
    nome = StringField('nome')
    cpf = StringField('cpf')
    email = EmailField('email')
    celular = StringField('celular')
    nomeUsuario = StringField('nomeUsuario')
    senha = password ('senha')
