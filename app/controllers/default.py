from app import app, db, lm
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required
import os
from flask import Flask, Response, request, abort, render_template_string, send_from_directory
from wtforms import Form,SelectMultipleField
from app.models.forms import LoginForm
from app.models.tables import User
from app.models.tables import Periodo
from app.models.tables import Disciplina
from app.models.forms import CadastroUsuarioForm
import numpy as np
import pandas as pd
from flask.ext.hashing import Hashing

#importando dados das disciplinas com o pandas
dados = pd.read_csv('../TCC/Analise_Pandas/dateset.csv')

@lm.user_loader
def load_user(id):
    return User.query.filter_by(id=id).first()

lm.login_view = "login"

lm.session_protection = "strong"

lm.login_message = u"Por favor insira o nome de usuário e senha para acessar !"

#lOGIN DO USUARIO
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

#CRUD USUARIO CADASTAR/ALTERAR/EXCLUIR
#CADASTRO
@app.route("/cadastroUsuario", methods=["GET", "POST"])
@login_required
def cadastroUsuario():
    cadastroform = CadastroUsuarioForm()
    if request.method == 'POST' and cadastroform.validate():
        user = User(cadastroform.nome.data,cadastroform.cpf.data,cadastroform.email.data,cadastroform.celular.data,
        cadastroform.nomeUsuario.data,cadastroform.tipo.data,cadastroform.senha.data)
        usuario = User.query.all()
        if User.query.all() == cadastroform.cpf.data:
            flash('Cpf já existente !')
            return redirect(url_for('listagemUsuario'))
        if User.query.all() == cadastroform.email.data:
            flash('E-mail já existente !')
            return redirect(url_for('listagemUsuario'))
        if User.query.all() == cadastroform.celular.data:
            flash('Celular já existente !')
            return redirect(url_for('listagemUsuario'))
        if User.query.all() == cadastroform.nomeUsuario.data:
            flash('Nome de Usuario já existente !')
            return redirect(url_for('listagemUsuario'))
        db.session.add(user)
        db.session.commit()

        flash('Usuário Cadastro com Sucesso !')
        return redirect(url_for('listagemUsuario'))
    return render_template('cadastroUsuarios.html',
                            cadastroform = cadastroform)

#EXCLUIR
@app.route("/excluirUsuario/<int:id>")
@login_required
def excluirUsuario(id):
    usuario = User.query.filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()
    usuarios = User.query.all()
    flash ("Dados Excluidos com Sucesso!")
    return redirect(url_for('listagemUsuario'))

#ALTERAR
@app.route("/atualizarUsuario/<int:id>", methods=["GET", "POST"])
@login_required
def atualizarUsuario(id):
    cadastroform = CadastroUsuarioForm()
    usuario = User.query.filter_by(id=id).first()
    #user = User(cadastroform.nome.data,cadastroform.cpf.data,cadastroform.email.data,cadastroform.celular.data,
    #cadastroform.nomeUsuario.data,cadastroform.tipo.data,cadastroform.senha.data)
    if cadastroform.nome.data:
        usuario.nome = cadastroform.nome.data
        usuario.cpf = cadastroform.cpf.data
        usuario.email = cadastroform.email.data
        usuario.celular = cadastroform.celular.data
        usuario.nomeUsuario = cadastroform.nomeUsuario.data
        usuario.tipo = cadastroform.tipo.data
        if cadastroform.senha.data != cadastroform.confirm.data:
            flash('Senhas não cofere !')
            flash('Retorne a pagina anterior para alterar ! !')
        if cadastroform.senha.data == cadastroform.confirm.data:
            usuario.senha = cadastroform.senha.data
            db.session.commit()
            flash('Usuário Alterado com Sucesso !')
            return redirect(url_for('listagemUsuario'))
    flash('Erro ao Alterar !')
    return render_template('atualizaUsuarios.html',
                            cadastroform = cadastroform)

#PAGINAS
#PAGINA INICIAL
@app.route("/index")
@login_required
def index():
    return render_template('index.html')

#PAGINA DE LOGOUL
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

#PAGINA listagem De Usuarios
@app.route("/listagem/<int:id>")
@login_required
def listagem(id):
    usuario = User.query.filter_by(id=id)
    cadastroform = CadastroUsuarioForm()
    return render_template('atualizaUsuarios.html',usuario=usuario, cadastroform=cadastroform)

@app.route("/listagemUsuario")
@login_required
def listagemUsuario():
    usuario = User.query.all()
    return render_template('listagemUsuarios.html',usuario=usuario)

#PAGINA EXCLUIR USUARIOS
@app.route("/excluir_Usuario")
@login_required
def excluir_Usuario():
    usuario = User.query.all()
    return render_template('excluirUsuarios.html',usuario=usuario)

#PAGINA INSERIR SITUAÇOES
@app.route("/inserirSituacoes")
@login_required
def inserirSituacoes():
    return render_template('inserirSituacoes.php')

#PAGINA DE RELATORIOS
@app.route("/relatorios")
@login_required
def relatorios():
    return render_template('relatorios.html')

#PAGINA DE AJUDA
@app.route("/ajuda")
@login_required
def ajuda():
        return render_template('ajuda.html')

#Analise com Panda e Numpy
@app.route("/disciplina")
@login_required
def disciplina():
        return render_template('disciplinas.html')

@app.route("/analise")
@login_required
def analise():
    dados.index.disciplina=None
    situacao = dados.loc[(dados.situacaoDisciplina=='REPROVADO')]
    return render_template('analise.html',tables=[situacao.to_html()], titles = ['na'])

@app.route("/disciplinasTads")
@login_required
def disciplinasTads():
    dados.set_index(['disciplina'])
    dados.index.disciplina=None
    Aprovado = dados.loc[dados.situacaoDisciplina=='APROVADO']
    Reprovado = dados.loc[dados.situacaoDisciplina=='REPROVADO']
    return render_template('disciplinasTads.html',tables=[Aprovado.to_html(classes='Aprovado'), Reprovado.to_html(classes='reprovado')],
    titles = ['na', 'Female surfers', 'Male surfers'])
    #disciplina = dados.groupby(['disciplina']).mean(), ('periodo')
    #return render_template('disciplinasTads.html',tables=[disciplina], titles = ['na'])

@app.route("/situacoes")
@login_required
def situacoes():
        disciplina = "TGA"
        situacaoDisciplina = "Aprovado"
        def resultados(disciplina,situacaoDisciplina):
            for i in range(1):
                probabilidadeTotal = dados.loc[(dados['disciplina']==disciplina)].count()
                probabilidade = dados.loc[(dados['disciplina']==disciplina) & (dados['situacaoDisciplina']==situacaoDisciplina)].count()
                a = probabilidade/probabilidadeTotal
                return "A probabilidaded  aluno ser ",situacaoDisciplina,'em', disciplina, a[i],'%'
            return render_template('inserirSituacoes.html')
