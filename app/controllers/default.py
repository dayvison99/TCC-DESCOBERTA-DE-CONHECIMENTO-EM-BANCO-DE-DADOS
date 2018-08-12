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
import numpy as np
import pandas as pd

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

lm.login_view = "login"

lm.session_protection = "strong"

lm.login_message = u"Por favor insira o nome de usuário e senha para acessar !"

#CRUD


@app.route("/excluirUsuario/<int:id>")
@login_required
def excluirUsuario(id):
    usuario = User.query.filter_by(id=id).first()
    #excluirUsuarioform = CadastroUsuarioForm()
    db.session.delete(usuario)
    db.session.commit()

    usuarios = User.query.all()
    flash ("Dados Excluidos com Sucesso!")
    return redirect(url_for('listagemUsuario'))
    #return render_template("listagemUsuarios.html",usuario=usuario)
#    excluirUsuarioform = CadastroUsuarioForm()
#    if request.method == 'POST' and excluirUsuarioform.validate():
#        user = User(excluirUsuarioform.nome.data,excluirUsuarioform.cpf.data,excluirUsuarioform.email.data,excluirUsuarioform.celular.data,
#        excluirUsuarioform.nomeUsuario.data,excluirUsuarioform.tipo.data,excluirUsuarioform.senha.data)
#        #,cadastroform.confirm.data)
#        db.session.delete(user)
#        db.session.commit()
#        flash('Cadastro Excluido com Sucesso !')
##    return render_template('cadastroUsuarios.html',
                            #cadastroform = cadastroform)


@app.route("/cadastroUsuario", methods=["GET", "POST"])
@login_required
def cadastroUsuario():
    cadastroform = CadastroUsuarioForm()
    if request.method == 'POST' and cadastroform.validate():
        user = User(cadastroform.nome.data,cadastroform.cpf.data,cadastroform.email.data,cadastroform.celular.data,
        cadastroform.nomeUsuario.data,cadastroform.tipo.data,cadastroform.senha.data)
        #,cadastroform.confirm.data)
        db.session.add(user)
        db.session.commit()
        flash('Usuário Cadastro com Sucesso !')
        return redirect(url_for('listagemUsuario'))
    return render_template('cadastroUsuarios.html',
                            cadastroform = cadastroform)

@app.route("/atualizarUsuario", methods=["GET", "POST"])
@login_required
def atualizarUsuario(id = id):
    cadastroform = CadastroUsuarioForm()
    if request.method == 'POST' and cadastroform.validate():
        user = User(cadastroform.nome.data,cadastroform.cpf.data,cadastroform.email.data,cadastroform.celular.data,
        cadastroform.nomeUsuario.data,cadastroform.tipo.data,cadastroform.senha.data)
        #,cadastroform.confirm.data)
        #db.session.add(user)
        db.session.commit()
        flash('Cadastro Atualizado com Sucesso !')
        return redirect(url_for('listagemUsuario'))
    return render_template('atualizaUsuarios.html',
                            cadastroform = cadastroform)


#Usuários admin
@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(nomeUsuario=form.username.data).first()
        if usuario and usuario.senha == form.password.data:
            login_user(usuario)
            flash("Bem Vindo!")
            return redirect(url_for('index'))
            if not is_safe_url('login.html'):
                return flask.abort(400)
        else:
            flash("Login ou Senha Incorretos!")
    return render_template('login.html',
                            form=form)

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
    usuario = User.query.all()
    return render_template('listagemUsuarios.html',usuario=usuario)

@app.route("/excluir_Usuario")
@login_required
def excluir_Usuario():
    usuario = User.query.all()
    return render_template('excluirUsuarios.html',usuario=usuario)

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

@app.route("/analise")
def analise():
    dados = pd.read_csv('../TCC/Analise_Pandas/dateset.csv')
    dados.index.disciplina=None
    situacao = dados.loc[(dados.situacaoDisciplina=='APROVADO')]
    return render_template('analise.html',tables=[situacao.to_html()], titles = ['na'])
