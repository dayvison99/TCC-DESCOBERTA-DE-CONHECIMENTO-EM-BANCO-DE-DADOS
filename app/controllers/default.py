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
#from flask.ext.hashing import Hashing



#importando banco de dados das disciplinas com o pandas
dados = pd.read_csv('../TCC/Analise_Pandas/dateset.csv')
disciplina_curso = pd.read_csv('../TCC/Analise_Pandas/disciplinacurso.csv')
disciplinamaiorreprovacao = pd.read_csv('../TCC/Analise_Pandas/disciplinamaiorreprovacao.csv')

##Fim importação##

#carregamento dos dados do usuario logado
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
            flash("Usuário ou Senha Incorretos!")
            flash("Contate o administrador do sistema caso não lembre a senha!")
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
        cpf = User.query.filter_by(cpf=cadastroform.cpf.data).first()
        if cpf and cpf.cpf == cadastroform.cpf.data:
            flash('Cpf já cadastrado !')
            return redirect(url_for('cadastroUsuario'))

        email = User.query.filter_by(email=cadastroform.email.data).first()
        if email and email.email == cadastroform.email.data:
            flash('E-mail cadastrado!')
            return redirect(url_for('listagemUsuario'))

        celular = User.query.filter_by(celular=cadastroform.celular.data).first()
        if celular and celular.celular == cadastroform.celular.data:
            flash('Celular cadastrado !')
            return redirect(url_for('listagemUsuario'))

        nomeUsuario = User.query.filter_by(nomeUsuario=cadastroform.nomeUsuario.data).first()
        if nomeUsuario and nomeUsuario.nomeUsuario == cadastroform.nomeUsuario.data:
            flash('Nome de Usuario já cadastrado!')
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

#esqueceu a senha
@app.route("/esqueceuSenha")
def esqueceuSenha():
    cadastroform = CadastroUsuarioForm
    return render_template('alterarSenha.html',
                            cadastroform = cadastroform)

@app.route("/alterarSenha", methods=["GET", "POST"])
def alterarSenha():
    cadastroform = CadastroUsuarioForm()
    usuario = User.query.all()
    if cadastroform.nome.data:
        if cadastroform.cpf.data != usuario.cpf:
            flash('Usuario não cadastrado')
            return redirect(url_for('alterarSenha'))
        if cadastroform.senha.data != cadastroform.confirm.data:
            flash('Senhas não cofere !')
            flash('Retorne a pagina anterior para alterar ! !')
        if cadastroform.senha.data == cadastroform.confirm.data:
            usuario.senha = cadastroform.senha.data
            db.session.commit()
            flash('Usuário Alterado com Sucesso !')
            return redirect(url_for('alterarSenha'))
    flash('Erro ao Alterar !')
    return render_template('login.html',
                            cadastroform = cadastroform)


#PAGINAS
#PAGINA INICIAL
@app.route("/index")
@login_required
def index():
    return render_template('index.html')

#PAGINA DE LOGOULT
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

#Listagem dos Usuarios cadastrados no sistema
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
@app.route("/inserirSituacoes", methods=["GET", "POST"])
@login_required
def inserirSituacoes():
    periodo = Periodo.query.all()
    disciplina = Disciplina.query.all()
    return render_template('inserirSituacoes.php', periodo=periodo, disciplina=disciplina)

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

##Parte da mineração de dados
#Analise da situaçoes com Panda e Numpy
@app.route("/analise")
@login_required
def analise():
    disciplinas = [('Algoritmo','REPROVADO'), ('TGA','APROVADO'),('Lingua_Portuguesa','APROVADO')]
    situacaoDisciplina = "Aprovado"
    def resultados(disciplinas): #disciplina,situacaoDisciplina
        a = []
        for d in disciplinas:
            probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
            probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
            a.append([d[0], d[1], probabilidade/probabilidadeTotal])
            msg = """A probabilidade do aluno obter um determinado resultado para as seguintes disciplinas:
            |          Disciplina         |    Situação  |    Probabilidade    |"""
            for i in a:
                msg+= '           |           {0}           |   {1}  |    {2}'.format(i[0], i[1], i[2])
                return msg
    return render_template('analise.html')

#Arvore de decisão sobre as situaçoes das disciplinas
@app.route("/situacoes")
@login_required
def situacoes():
        disciplinas = [('Algoritmo','REPROVADO'), ('TGA','APROVADO'),('Lingua_Portuguesa','APROVADO')]
        situacaoDisciplina = "Aprovado"
        def resultados(disciplinas): #disciplina,situacaoDisciplina
            a = []
            for d in disciplinas:
                probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                a.append([d[0], d[1], probabilidade/probabilidadeTotal])
                msg = """A probabilidade do aluno obter um determinado resultado para as seguintes disciplinas:
                |          Disciplina         |    Situação  |    Probabilidade    |"""
                for i in a:
                    msg+= '           |           {0}           |   {1}  |    {2}'.format(i[0], i[1], i[2])
                    return msg
                return render_template('inserirSituacoes.php')
        return render_template('inserirSituacoes.php')

#### Relatorios do Sistema ####

#relatorios de usuarios cadastrados
@app.route("/usuariosCadastrados")
@login_required
def usuariosCadastrados():
        usuario = User.query.order_by(User.nome).all()
        cadastroform = CadastroUsuarioForm()
        return render_template('relatorioUsuarios.html',usuario=usuario, cadastroform=cadastroform)

#Relatorios Disciplinas do curso de Tads
@app.route("/disciplinasTads")
@login_required
def disciplinasTads():
    #resultado = dados.groupby(['disciplina']).describe()
    #resultado = resultado.filter(items=['disciplina'])
    resultado = disciplina_curso.groupby(['disciplina']).max()
    resultado = resultado = resultado.sort_values(by=['periodo'])
    resultado = resultado.rename(columns={'periodo' : 'Periodo da Disciplina'})
    return render_template('disciplinas.html',tables=[resultado.to_html(classes='table table-striped')],
    titles = ['na'])

#Situaçoes Das Disciplinas
@app.route("/disciplinaAprovacao")
@login_required
def disciplinaAprovacao():
    consulta = disciplinamaiorreprovacao.query('situacaoDisciplina == "APROVADO"')
    resultado = consulta.groupby(['disciplina']).count()
    resultado = resultado.sort_values(by=['situacaoDisciplina'], ascending =False)
    resultado = resultado.rename(columns={'situacaoDisciplina' : 'Quantidade de Aprovações'})
    return render_template('disciplinas.html',tables=[resultado.to_html(classes='table table-striped')],
    titles = ['na'])

#Situaçoes Das Disciplinas
@app.route("/disciplina")
@login_required
def disciplina():
    consulta = disciplinamaiorreprovacao.query('situacaoDisciplina == "REPROVADO"')
    resultado = consulta.groupby(['disciplina']).count()
    resultado = resultado.sort_values(by=['situacaoDisciplina'], ascending =False)
    resultado = resultado.rename(columns={'situacaoDisciplina' : 'Quantidade de Reprovações'})
    return render_template('disciplinas.html',tables=[resultado.to_html(classes='table table-striped')],
    titles = ['na'])

#Situaçoes Das Disciplinas
@app.route("/disciplinaDesistencia")
@login_required
def disciplinaDesistencia():
    consulta = disciplinamaiorreprovacao.query('situacaoDisciplina == "CANCELADO"')
    resultado = consulta.groupby(['disciplina']).count()
    resultado = resultado.sort_values(by=['situacaoDisciplina'], ascending =False)
    resultado = resultado.rename(columns={'situacaoDisciplina' : 'Quantidade de Desistência'})
    return render_template('disciplinas.html',tables=[resultado.to_html(classes='table table-striped')],
    titles = ['na'])

#Situaçoes Das Disciplinas
@app.route("/mediaMatricula")
@login_required
def mediaMatricula():
    consulta = disciplinamaiorreprovacao.query('situacaoDisciplina == "MATRICULADO"')
    resultado = consulta.groupby(['disciplina']).count()
    resultado = resultado.sort_values(by=['situacaoDisciplina'], ascending =False)
    resultado = resultado.rename(columns={'situacaoDisciplina' : 'Média de Matriculas'})
    return render_template('disciplinas.html',tables=[resultado.to_html(classes='table table-striped')],
    titles = ['na'])
