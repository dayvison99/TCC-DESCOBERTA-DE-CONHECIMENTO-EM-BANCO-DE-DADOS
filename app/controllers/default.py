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
    #return User(id)
    return User.query.filter_by(id=id).first()



@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(nomeUsuario=form.username.data).first()
        if usuario and usuario.senha == form.password.data:
            login_user(usuario)
            flash("Bem Vindo!")
            return redirect(url_for("index"))
        else:
            flash("Login ou Senha Incorretos!")
    return render_template('login.html',
                            form=form)

@app.route("/cadastroUsuario", methods=["GET", "POST"])
def cadastroUsuario():
    cadastroform = CadastroUsuarioForm()
    return render_template('cadastroUsuarios.html',
                            cadastroform = cadastroform)


@app.route("/index")

def index():
    return render_template('index.html')

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))


#def logout():
#    return redirect(url_for("login"))
#    logout_user()

@app.route("/listagemUsuario")
def listagemUsuario():
    return render_template('listagemUsuarios.html')


@app.route("/inserirSituacoes")
def inserirSituacoes():
    return render_template('inserirSituacoes.html')

@app.route("/relatorios")
def relatorios():
    return render_template('relatorios.html')

@app.route("/ajuda")
def ajuda():
        return render_template('')
