from app import app, db, lm
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user
import os
from flask import Flask, Response, request, abort, render_template_string, send_from_directory

from app.models.forms import LoginForm
from app.models.tables import User

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()



@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(nomeUsuario=form.username.data).first()
        if user and user.senha == form.password.data:
            login_user(user)
            flash("Bem Vindo!")
            return redirect(url_for("index"))
        else:
            flash("Login ou Senha Incorretos!")
    return render_template('login.html',
                            form=form)


@app.route("/index")

def index():
    return render_template('index.html')

@app.route("/logout")
def logout():
    return redirect(url_for("login"))
    logout_user()

@app.route("/cadastroUsuario")
def cadastroUsuario():
    return render_template('cadastroUsuarios.html')

@app.route("/inserirSituacoes")
def inserirSituacoes():
    return render_template('inserirSituacoes.html')

@app.route("/relatorios")
def relatorios():
    return render_template('relatorios.html')
