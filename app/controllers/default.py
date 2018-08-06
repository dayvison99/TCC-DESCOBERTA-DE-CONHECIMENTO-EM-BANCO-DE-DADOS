from app import app, db, lm
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
import os
from flask import Flask, Response, request, abort, render_template_string, send_from_directory
from wtforms import Form
from app.models.forms import LoginForm
from app.models.tables import User
from app.models.tables import Periodo
from app.models.tables import Disciplina
from app.models.forms import CadastroUsuarioForm


@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

lm.login_view = "login"

lm.session_protection = "strong"

lm.login_message = u"Por favor insira o nome de usuário e senha para acessar !"

@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(nomeUsuario=form.username.data).first()
        if usuario and usuario.senha == form.password.data:
            login_user(usuario)
            flash("Bem Vindo!")
            #tipoUser = User.query.filter_by(tipo=form.tipo.data).first()
            if usuario.tipo == "admin":
                return redirect(url_for('index'))
            else:
                return redirect(url_for('cadastroUsuario'))
            if not is_safe_url(next):
                return flask.abort(400)
        else:
            flash("Login ou Senha Incorretos!")
    return render_template('login.html',
                            form=form)

@app.route("/cadastroUsuario", methods=["GET", "POST"])
@login_required
def cadastroUsuario():
    cadastroform = CadastroUsuarioForm()
    if request.method == 'POST' and cadastroform.validate():
        user = User(cadastroform.name.data, cadastroform.cpf.data,cadastroform.email.data,
        cadastroform.celular.data,cadastroform.nomeUsuario.data,
                    cadastroform.senha.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('cadastroUsuarios.html',
                            cadastroform = cadastroform)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User(form.username.data, form.email.data,
                    form.password.data)
        db_session.add(user)
        flash('Thanks for registering')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)




@app.route("/index")
@login_required
def index():
    return render_template('index.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

@app.route("/listagemUsuario")
@login_required
def listagemUsuario():
    return render_template('listagemUsuarios.html')


@app.route("/inserirSituacoes")
@login_required
def inserirSituacoes():
    return render_template('inserirSituacoes.html')

@app.route("/relatorios")
@login_required
def relatorios():
    return render_template('relatorios.html')

@app.route("/ajuda")
@login_required
def ajuda():
        return render_template('')
