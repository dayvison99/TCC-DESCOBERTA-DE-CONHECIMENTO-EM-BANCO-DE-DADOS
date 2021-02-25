#importando bibliotecas do flask
from app import app, db, lm
from flask import Flask, Response, request, abort, render_template_string, send_from_directory,render_template, flash, redirect, url_for, request, session
from flask_login import login_user, logout_user, login_required
from wtforms import Form,SelectMultipleField,StringField, HiddenField, SelectField, FormField, BooleanField, FieldList, PasswordField
from app.models.forms import Disciplinas_AlunosForm,LoginForm,CadastroUsuarioForm,AlunosForm,DisciForm, SituacaoDisciplinaForm
from app.models.tables import User,Periodo,Disciplina,Alunos,Disciplinas_Alunos, SituacaoDisciplinas
from flask_session import Session
from sqlalchemy.sql import func
import hashlib
import os
from flask_weasyprint import HTML, render_pdf

#importando bibliotecas de manipulação de dados
import numpy as np
import pandas as pd

#chave de seguranca
app.SECRET_KEY = "secreta123"

#importando banco de dados das disciplinas com o pandas
dados = pd.read_csv('../TCC/Analise_Pandas/dateset.csv')
disciplina_curso = pd.read_csv('../TCC/Analise_Pandas/disciplinacurso.csv')
disciplinamaiorreprovacao = pd.read_csv('../TCC/Analise_Pandas/disciplinamaiorreprovacao.csv')

##conectando bd para relatorios
import pymysql
conexao = pymysql.connect(db='data', user='root', passwd='secreta123')
cursor = conexao.cursor()

##Fim importação##

#carregamento dos dados do usuario logado
@lm.user_loader
def load_user(id):
    session["idpadrao"] = id
    return User.query.filter_by(id=id).first()

lm.login_view = "login"

lm.session_protection = "strong"

lm.login_message = u"Por favor insira o nome de usuário e senha para acessar !"

#Manual
@app.route("/manual", methods=["GET", "POST"])
@login_required
def manual():
    return redirect(url_for('leiame'))

#lOGIN DO USUARIO
@app.route("/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = User.query.filter_by(nomeUsuario=form.username.data).first()
        if usuario and usuario.senha == form.password.data:
            login_user(usuario, remember=True)
            flash("Bem vindo " +usuario.nomeUsuario)
            return redirect(url_for('index'))
            if not is_safe_url('login.html'):
                return flask.abort(400)
        else:
            flash("Usuário ou Senha Incorretos!")
            flash("Contate o administrador do sistema caso não lembre a senha!")
    return render_template('login.html',
                            form=form)

#CRUD USUARIO CADASTAR/ALTERAR/EXCLUIR

#Cadastro de USUARIOS
@app.route("/cadastroUsuario", methods=["GET", "POST"])
@login_required
def cadastroUsuario():
    cadastroform = CadastroUsuarioForm()
    session['nomeU'] = request.form.get("nome")
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

        user.nome = user.nome.upper()
        db.session.add(user)
        db.session.commit()

        flash('Usuário Cadastrado com Sucesso !')
        return redirect(url_for('listagemUsuario'))
    return render_template('cadastroUsuarios.html',
                            cadastroform = cadastroform)

#EXCLUIR usuarios
@app.route("/excluirUsuario/<int:id>")
@login_required
def excluirUsuario(id):
    usuario = User.query.filter_by(id=id).first()
    db.session.delete(usuario)
    db.session.commit()
    usuarios = User.query.all()
    flash ("Dados Excluidos com Sucesso!")
    return redirect(url_for('listagemUsuario'))

#Alterar dados do usuarios
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
            usuario.nome = usuario.nome.upper()
            db.session.commit()
            flash('Usuário Alterado com Sucesso !','danger')
            return redirect(url_for('listagemUsuario'))
    flash('Erro ao Alterar !')
    return render_template('atualizaUsuarios.html',
                            cadastroform = cadastroform)

#Alterar dados do usuarios Padrao
@app.route("/atualizarUsuarioPadrao/<int:id>", methods=["GET", "POST"])
@login_required
def atualizarUsuarioPadrao(id):
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
            usuario.nome = usuario.nome.upper()
            db.session.commit()
            flash('Usuário Alterado com Sucesso !','danger')
            return redirect(url_for('listagemPadrao'))
    flash('Erro ao Alterar !')
    return render_template('atualizaUsuarios.html',
                            cadastroform = cadastroform)

#Alterar a senha na tela de login
@app.route("/esqueceuSenha/",methods=["GET", "POST"])
def esqueceuSenha():
    cadastroform = CadastroUsuarioForm()
    cpf = User.query.filter_by(cpf=cadastroform.cpf.data).first()
    email = User.query.filter_by(email=cadastroform.email.data).first()

    if request.method == 'POST':
        if cpf and cpf.cpf == cadastroform.cpf.data and email and email.email == cadastroform.email.data:
            a = User.query.filter_by(cpf=cadastroform.cpf.data).first()
            id = a.id
            usuario = User.query.filter_by(id=id).first()
            usuario.cpf = cadastroform.cpf.data
            usuario.email = cadastroform.email.data

            if cadastroform.senha.data != cadastroform.confirm.data:
                flash('Senhas não cofere !')
                flash('Por favor corrigir a senha digitada  !')
            if cadastroform.senha.data == cadastroform.confirm.data and cadastroform.senha.data != "" :
                usuario.senha = cadastroform.senha.data
                usuario.nome = usuario.nome.upper()
                db.session.commit()
                flash('Senha Alterada com Sucesso !')
                return redirect(url_for('login'))
            else:
                flash("Campo senha não pode ser vazio")
        else:
            flash('Usuario não encontrado')
    return render_template('alterarSenha.html',cadastroform = cadastroform)

#Menus para acessar as paginas

#PAGINA INICIAL
@app.route("/index")
@login_required
def index():
    return render_template('index.html')

@app.route("/leiame")
def leiame():
    return render_template('leiame.html')

#PAGINA DE LOGOULT
@app.route("/logout")
@login_required
def logout():
    logout_user()
    session["salvardisciplina"] = None
    session["salvarstatus"] = None
    session["cont"] = 0
    session["aux"] = None
    session["lista"] = None
    session["listaAux"] = None
    session["listaMaterias"] = None
    session["listaAuxMaterias"] = None
    return redirect(url_for("login"))

#Pagina que listagem  Usuario selecionaodo
@app.route("/listagem/<int:id>")
@login_required
def listagem(id):
    usuario = User.query.filter_by(id=id)
    cadastroform = CadastroUsuarioForm()
    return render_template('atualizaUsuarios.html',usuario=usuario, cadastroform=cadastroform)

#Pagina altera  Usuario padrao
@app.route("/listagemPadrao")
@login_required
def listagemPadrao():
    usuario = User.query.filter_by(id=session["idpadrao"])
    cadastroform = CadastroUsuarioForm()
    return render_template('atualizaUsuariosPadrao.html',usuario=usuario, cadastroform=cadastroform)

#Listagem de todos os Usuarios cadastrados no sistema
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
@app.route("/inserirSituacoes/<int:id>", methods=["GET", "POST"])
@login_required
def inserirSituacoes(id):
    alunos = Alunos.query.filter_by(id = id).first()
    flash("ALUNO(A) SELECIONADO " + alunos.nome)
    if alunos.curso == "TADS":
        session["idAluno"] = alunos.cpf
        periodo = Periodo.query.all()
        disciplina = Disciplina.query.all()
    else:
        session["idAluno"] = alunos.cpf
        periodo = Periodo.query.all()
        disciplina = Disciplina.query.filter(Disciplina.equibsi!="")
        usuario = User.query.filter_by(id=session["idpadrao"])
    return render_template('inserirSituacoes.html', periodo=periodo, disciplina=disciplina)

#inserir situaçoes
@app.route("/inserir/<int:id>", methods=["GET", "POST"])
@login_required
def inserir(id):
    periodo = Periodo.query.all()
    disciplina = Disciplina.query.filter_by(periodo = id)
    return render_template('inserirSituacoes.html', periodo=periodo, disciplina=disciplina)

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

#PAGINA DE NOSSAS HISTORIA
@app.route("/nossahistoriatads")
@login_required
def nossahistoriatads():
        return render_template('nossaHistoria.html')

@app.route("/nossahistoriabsi")
@login_required
def nossahistoriabsi():
        return render_template('nossaHistoriabsi.html')

@app.route("/nossahistoriaifnmg")
@login_required
def nossahistoriaifnmg():
        return render_template('nossaHistoriaifnmg.html')

#####Alunos

@app.route("/todosAlunos")
@login_required
def todosAlunos():
    alunos = Alunos.query.all()
    return render_template('buscarAlunos.html',alunos=alunos)

# Salvando dados alunos apos analise
@app.route("/listagemAlunos", methods=["GET", "POST"])
@login_required
def listagemAlunos():
    alunosform = AlunosForm()
    alunos = Alunos.query.filter_by(cpf=session["idAluno"]).first()
    if alunos:
        alunos.media = 0
        alunos.resultado = session['resultados']
        resultado = alunos.resultado
        disAlunos = Disciplinas_AlunosForm()
        disciplinas_alunos = Disciplinas_Alunos(disAlunos.id_disciplinas.data,disAlunos.nomeDisciplina.data,disAlunos.id_alunos.data, disAlunos.resultado.data)
        disciplinas_alunos.id_alunos = alunos.id
        disciplinas_alunos.id_disciplinas = session["disciplinas_id"]
        disciplinas_alunos.resultado=alunos.resultado
        resultado = alunos.resultado
        media = Disciplinas_Alunos.query.with_entities(func.avg(Disciplinas_Alunos.resultado).label('average')).filter(Disciplinas_Alunos.id_alunos==alunos.id).group_by(Disciplinas_Alunos.id_alunos)
        alunos.media = media
        disciplinas_alunos.nomeDisciplina = session['disciplina_aux']

        dnome = Disciplinas_Alunos.query.filter_by(id_disciplinas=session['disciplina_aux']).first()
        daluno = Disciplinas_Alunos.query.filter_by(id_alunos=alunos.id).first()
        #Verificando se a analise ja foi feita para determinado aluno
        if dnome and daluno :
            if dnome.nomeDisciplina == session["disciplinas_id"] and daluno.id_alunos == alunos.id :
                flash("Disciplina Já Analizada para o aluno selecionado!")
                return redirect(url_for('inserirSituacoes',id = alunos.id))

        alunos.nome=alunos.nome.upper()
        db.session.add(alunos)
        db.session.add(disciplinas_alunos)
        db.session.commit()
        flash('DADOS DO ALUNO SELECIONADO SALVOS COM SUCESSO!','danger')
        alunos.media = media
        db.session.add(disciplinas_alunos)
        db.session.commit()
        return redirect(url_for('inserirSituacoes',id = alunos.id))
    if request.form.get("cpf") != None:
        flash("Aluno não encontrado, por favor verifique o cpf!")
    return render_template('salvaralunos.html',
                            alunosform=alunosform)

#listando todos os alunos com analise salvas
@app.route("/alunosAnalise/",methods=["GET", "POST"])
@login_required
def alunosAnalise():
    dAluno = Disciplinas_AlunosForm()
    alunosform = AlunosForm()
    dialuno = Disciplinas_Alunos.query.all()
    #session["dialuno1"]= dialuno
    alunos = Alunos.query.all()
    alunos= Alunos.query.filter(Alunos.resultado > 0).order_by(Alunos.nome)
    #session["aluno1"]= alunos
    return render_template('listagemAlunos.html',alunos=alunos,dialuno=dialuno)

#listando qual o risco em cada disciplina
@app.route("/percentualdisci1/",methods=["GET", "POST"])
@login_required
def percentualdisci1():
    alunos = Alunos.query.all()
    return render_template('listAlunosDisci.html',alunos=alunos)

@app.route("/percentualdisci/<int:id>",methods=["GET", "POST"])
@login_required
def percentualdisci(id):
    alunosform = AlunosForm()
    daform = Disciplinas_AlunosForm()
    disForm = DisciForm()
    alunos = Alunos(alunosform.nome.data,alunosform.cpf.data,alunosform.resultado.data,alunosform.media.data)
    alunos = Alunos.query.filter(Alunos.id==id)
    session["a1"] = id
    aluno = Alunos.query.filter_by(id=id).first()
    if aluno:
        if aluno.id==id:
            disAlunos = Disciplinas_Alunos(daform.id_disciplinas.data,daform.nomeDisciplina,daform.resultado.data,daform.id_alunos.data)
            disAlunos = Disciplinas_Alunos.query.filter(Disciplinas_Alunos.id_alunos==aluno.id)
            return render_template('listAlunosDisciRelatorio.html',
            alunos=alunos,disAlunos=disAlunos)
    else:
        flash("Aluno não encontrado, por favor verifique o cpf!")
        return render_template('listAlunosDisci.html')

#listando todos os alunos com risco de evasão
@app.route("/alunosRisco/",methods=["GET", "POST"])
@login_required
def alunosRisco():
    id = request.form.get("select")
    session["riscoid"]= id
    if id:
        alunosform = AlunosForm()
        alunos = Alunos.query.all()
        alunos = Alunos.query.filter(Alunos.media >=id ).order_by(Alunos.media.desc())
        return render_template('listagemAlunosrisco.html',alunos=alunos)
    else:
        id = 0
        session["riscoid"]= id
        alunosform = AlunosForm()
        alunos = Alunos.query.filter(Alunos.media >=0.1 ).order_by(Alunos.media.desc())
        return render_template('listagemAlunosrisco.html',alunos=alunos)

#Excluir lista de alunos
@app.route("/excluirAlunos/<int:id>",methods=["GET", "POST"])
@login_required
def excluirAlunos(id):
    cont = 0
    while cont < 1:
        disAlunos = Disciplinas_Alunos.query.filter_by(id_alunos=id).first()
        if disAlunos:
            cont = cont-1
            alunosform = AlunosForm()
            daform = Disciplinas_AlunosForm()
            alunos = Alunos.query.filter_by(id=id).first()
            alunos.resultado = 0
            alunos.media = 0
            db.session.delete(disAlunos)
            db.session.commit()
            alunos = Alunos.query.all()
            disAlunos = Disciplinas_Alunos.query.all()
        cont = cont+1
    flash ("Dados Excluidos com Sucesso!")
    return redirect(url_for('alunosAnalise'))

##Parte da mineração de dados
#armazenado dados
@app.route("/sessao/",methods=["GET", "POST"])
@login_required
def sessao():
    id = request.form.get("disciplina")
    session["salvardisciplina"] = request.form.get("disciplina")
    session["salvarstatus"] = request.form.get("status")
    session["disciplinas_id"]= id
    session['disciplina_aux'] = request.form.get("disciplina")
    periodo = Periodo.query.all()
    disciplina = Disciplina.query.all()
    amazenamento = []
    if request.form.get("disciplina") and request.form.get("status") is not None:
        materias = Disciplina.query.filter_by(id = id).first()
        situacaoDisciplina = request.form.get("status")
        disciplinas = [(materias.nomeData,situacaoDisciplina)]
        amazenamento.append(disciplinas)
        session["aux"] = amazenamento
        return redirect(url_for('analise'))
        #return render_template('finalizarSituacoes.html',tables=[materias.nome,session["salvarstatus"]],
        #titles = ['na','Disciplinas', 'Situações'],periodo=periodo, disciplina=disciplina)

    if request.form.get("disciplina") is None:
        flash("Escolha uma Disciplina")
        return render_template('inserirSituacoes.html',
        titles = ['na'],periodo=periodo, disciplina=disciplina)

    if request.form.get("status") is None:
        flash("Escolha uma Situação")
        return render_template('salvaralunos.html',
        titles = ['na'],periodo=periodo, disciplina=disciplina)

#Analise da situaçoes com Panda e Numpy
@app.route("/analise/",methods=["GET", "POST"])
@login_required
def analise():
    if session["salvardisciplina"] and session["salvarstatus"] is not None:
        id = session["salvardisciplina"]
        situacaoDisciplina = session["salvarstatus"]
        materias = Disciplina.query.filter_by(id = id).first()
        flash("Probabilidades para a disciplina " + materias.nome)
        disciplinas = [(materias.nomeData,situacaoDisciplina)]
        b = []
        a = []
        c = 0
        cont=0
        for d in disciplinas:
            if situacaoDisciplina == 'REPROVADO':
                cont=cont+1
                probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                probabilidade= probabilidade*100
                a.append([d[0], probabilidade/probabilidadeTotal])
                prob = dados.loc[(dados['disciplina']==d[0])].count()
                for i in range(1):
                        probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                        probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                        b = probabilidade/probabilidadeTotal*100
                        c = b+c
                reprovado = round(c[0]/cont, 2)
                aprovado =  round(100-c[0]/cont, 2)
            if situacaoDisciplina == 'APROVADO':
                cont=cont+1
                probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                probabilidade= probabilidade*100
                a.append([d[0], probabilidade/probabilidadeTotal])
                prob = dados.loc[(dados['disciplina']==d[0])].count()
                for i in range(1):
                        probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                        probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                        b = probabilidade/probabilidadeTotal*100
                        c = b+c
                reprovado = round(c[0]/cont, 2)
                aprovado =  round(100-c[0]/cont, 2)

            if situacaoDisciplina == 'MATRICULADO':
                cont=cont+1
                probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                probabilidade= probabilidade*100
                a.append([d[0], probabilidade/probabilidadeTotal])
                prob = dados.loc[(dados['disciplina']==d[0])].count()
                for i in range(1):
                        probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                        probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                        b = probabilidade/probabilidadeTotal*100
                        c = b+c
                reprovado = round(c[0]/cont, 2)
                aprovado =  round(100-c[0]/cont, 2)
            if situacaoDisciplina == 'CANCELADO':
                cont=cont+1
                probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                probabilidade= probabilidade*100
                a.append([d[0], probabilidade/probabilidadeTotal])
                prob = dados.loc[(dados['disciplina']==d[0])].count()
                for i in range(1):
                        probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                        probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                        b = probabilidade/probabilidadeTotal*100
                        c = b+c
                reprovado = round(c[0]/cont, 2)
                aprovado =  round(100-c[0]/cont, 2)

            else:
                cont=cont+1
                valorTotal = total=dados['situacaoDisciplina'].count()
                probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                probabilidade= probabilidade*100
                a.append([d[0], probabilidade/probabilidadeTotal])
                prob = dados.loc[(dados['disciplina']==d[0])].count()
                for i in range(1):
                        probabilidadeTotal = dados.loc[(dados['disciplina']==d[0])].count()
                        probabilidade = dados.loc[(dados['disciplina']==d[0]) & (dados['situacaoDisciplina']==d[1])].count()
                        b = probabilidade/probabilidadeTotal*100
                        c = b+c

                reprovado = round(c[0]/cont, 2)
                aprovado =  round(100-c[0]/cont, 2)

        j=round(c[0]/cont, 2)
        session["resultados"] = j

         #Alerta de aluno com risco de Reprovação
        if reprovado > 60:
            flash("Atenção!!")
            flash("Aluno com probabilidades de Reprovação acima de 60 %")
        session["auxDisciplina"] = session["salvardisciplina"]
        session["auxStatus"] = None
        session["salvardisciplina"] = None
        session["salvarstatus"] = None
        session["cont"] = 0
        session["aux"] = None
        if situacaoDisciplina == 'REPROVADO':
            return render_template('analise.html',tables=[reprovado],
            titles = ['na','Probabilidade de Reprovação Para o Aluno'])
        if situacaoDisciplina == 'APROVADO':
            return render_template('analise.html',tables=[aprovado],
            titles = ['na',' Probabilidade de Aprovação Para o Aluno,'])
        if situacaoDisciplina == 'CANCELADO':
            return render_template('analise.html',tables=[reprovado],
            titles = ['na',' Probabilidade de Reprovação Para o Aluno,'])
        if situacaoDisciplina == 'MATRICULADO':
            return render_template('analise.html',tables=[reprovado],
            titles = ['na',' Probabilidade de Reprovação Para o Aluno,'])

        return render_template('analise.html')
    else:
        periodo = Periodo.query.all()
        disciplina = Disciplina.query.all()
        flash("Insira as Disciplinas e as Situaçoes antes de Finalizar")
        return render_template('inserirSituacoes.html',
        titles = ['na'],periodo=periodo, disciplina=disciplina)


#Arvore de decisão sobre as situaçoes das disciplinas
@app.route("/situacoes/",methods=["GET", "POST"])
@login_required
def situacoes():
        disciplinas = session["salvardisciplina"]
        situacaoDisciplina = session["salvarstatus"]
        def resultados(disciplinas):
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
                return render_template('inserirSituacoes.html')
        return render_template('inserirSituacoes.html')

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
    resultado = Disciplina.query.filter().group_by(Disciplina.nome).order_by(Disciplina.periodo)
    return render_template('disciplinas.html',resultado = resultado)

#Situaçoes Das Disciplinas
@app.route("/disciplinaAprovacao",methods=["GET", "POST"])
@login_required
def disciplinaAprovacao():
    session["pdfStatus"] = "Aprovações"
    datai = request.form.get('datai')
    dataf = request.form.get('dataf')
    session["datai"] = datai
    session["dataf"] = dataf
    if datai and dataf is not None:
        if datai > dataf:
            flash("Data Inicial Não Pode Ser Maior que Data Final")
            return render_template('disciplinasmaioraprovacao.html')
        else:
            cursor.execute("SELECT disciplina,COUNT(situacaoDisciplina),data, periodo FROM situacaoDisciplinas WHERE situacaoDisciplina like 'APROVADO' and  data between \'"+datai+"\' and \'"+dataf+"\' group by disciplina order by count(situacaoDisciplina) desc ")
            resultado = cursor.fetchall()
            session['pdfAprovado'] = resultado
            return render_template('disciplinasmaioraprovacao.html',resultado = resultado)
    else:
        session["datai"] = "01-01-2007"
        session["dataf"] = "31-12-2018"
        cursor.execute("SELECT disciplina,COUNT(situacaoDisciplina),data, periodo FROM situacaoDisciplinas WHERE situacaoDisciplina like 'APROVADO' group by disciplina order by count(situacaoDisciplina) desc ")
        resultado = cursor.fetchall()
        session['pdfAprovado'] = resultado
        return render_template('disciplinasmaioraprovacao.html',resultado = resultado  )

#Situaçoes Das Disciplinas
@app.route("/disciplina",methods=["GET", "POST"])
@login_required
def disciplina():
    session["pdfStatus"] = "Reprovações"
    datai = request.form.get('datai')
    dataf = request.form.get('dataf')
    session["datai"] = datai
    session["dataf"] = dataf
    if datai and dataf is not None:
        if datai > dataf:
            flash("Data Inicial Não Pode Ser Maior que Data Final")
            return render_template('disciplinasmaiorreprovacao.html')
        else:
            cursor.execute("SELECT disciplina,COUNT(situacaoDisciplina),data, periodo FROM situacaoDisciplinas WHERE situacaoDisciplina like 'REPROVADO' and  data between \'"+datai+"\' and \'"+dataf+"\' group by disciplina order by count(situacaoDisciplina) desc ")
            resultado = cursor.fetchall()
            session['pdfAprovado'] = resultado
            return render_template('disciplinasmaiorreprovacao.html',resultado = resultado)
    else:
        session["datai"] = "01-01-2007"
        session["dataf"] = "31-12-2018"
        cursor.execute("SELECT disciplina,COUNT(situacaoDisciplina),data, periodo FROM situacaoDisciplinas WHERE situacaoDisciplina like 'REPROVADO' group by disciplina order by count(situacaoDisciplina) desc ")
        resultado = cursor.fetchall()
        session['pdfAprovado'] = resultado
        return render_template('disciplinasmaiorreprovacao.html',resultado = resultado  )


#Situaçoes Das Disciplinas
@app.route("/disciplinaDesistencia",methods=["GET", "POST"])
@login_required
def disciplinaDesistencia():
    session["pdfStatus"] = "Desistências"
    datai = request.form.get('datai')
    dataf = request.form.get('dataf')
    session["datai"] = datai
    session["dataf"] = dataf
    if datai and dataf is not None:
        if datai > dataf:
            flash("Data Inicial Não Pode Ser Maior que Data Final")
            return render_template('disciplinasdesistencia.html')
        else:
            cursor.execute("SELECT disciplina,COUNT(situacaoDisciplina),data, periodo FROM situacaoDisciplinas WHERE situacaoDisciplina like 'CANCELADO' and  data between \'"+datai+"\' and \'"+dataf+"\' group by disciplina order by count(situacaoDisciplina) desc ")
            resultado = cursor.fetchall()
            session['pdfAprovado'] = resultado
            return render_template('disciplinasdesistencia.html',resultado = resultado)
    else:
        session["datai"] = "01-01-2007"
        session["dataf"] = "31-12-2018"
        cursor.execute("SELECT disciplina,COUNT(situacaoDisciplina),data, periodo FROM situacaoDisciplinas WHERE situacaoDisciplina like 'CANCELADO' group by disciplina order by count(situacaoDisciplina) desc ")
        resultado = cursor.fetchall()
        session['pdfAprovado'] = resultado
        return render_template('disciplinasdesistencia.html',resultado = resultado  )


#Situaçoes Das Disciplinas
@app.route("/mediaMatricula")
@login_required
def mediaMatricula():
    consulta = disciplinamaiorreprovacao.query('situacaoDisciplina == "MATRICULADO"')
    resultado = consulta.groupby(['disciplina']).count()
    resultado = resultado.sort_values(by=['situacaoDisciplina'], ascending =False)
    resultado = resultado.rename(columns={'situacaoDisciplina' : 'Média de Matriculas'})
    return render_template('disciplinasmedia.html',tables=[resultado.to_html(classes='table table-striped')],
    titles = ['na'])

@app.route("/ingressoCidade")
@login_required
def ingressoCidade():
    cursor.execute("SELECT matricula.status,matricula.cidade, Round(count(matricula.status)/281*100,2) as Porcentagem FROM matricula,ingresso where(matricula.status like '%CONCLU%' or matricula.status like 'ABANDONO' or matricula.status like 'DESLIGADO') and matricula.matricula = ingresso.aluno_id group by matricula.status,matricula.cidade order by Porcentagem desc")
    resultado = cursor.fetchall()
    return render_template('ingressoCidade.html',resultado = resultado  )

@app.route("/formasIngresso")
@login_required
def formasIngresso():
    cursor.execute("SELECT matricula.status,ingresso.forma_ingresso, Round(count(matricula.status)/281*100,2) as Porcentagem FROM matricula,ingresso where(matricula.status like '%CONCLU%' or matricula.status like 'ABANDONO' or matricula.status like 'DESLIGADO') and matricula.matricula = ingresso.aluno_id group by matricula.status, ingresso.forma_ingresso order by Porcentagem desc")
    resultado = cursor.fetchall()
    return render_template('formasingresso.html',resultado = resultado  )

@app.route("/rendimento")
@login_required
def rendimento():
    cursor.execute("SELECT ingresso.coeficiente_rendimento,matricula.status, turma.nome FROM matricula,ingresso, turma where(matricula.status like '%CONCLU%' or matricula.status like 'ABANDONO' or matricula.status like 'DESLIGADO') and matricula.matricula = ingresso.aluno_id and turma.id =  ingresso.turma_id and turma.nome like '%TL%' order by coeficiente_rendimento desc ")
    resultado = cursor.fetchall()
    return render_template('rendimento.html',resultado = resultado  )


#Ralatorios em PDFS
@app.route('/pdfcidade')
def pdfcidade():
    cursor.execute("SELECT matricula.status,matricula.cidade, Round(count(matricula.status)/281*100,2) as Porcentagem FROM matricula,ingresso where(matricula.status like '%CONCLU%' or matricula.status like 'ABANDONO' or matricula.status like 'DESLIGADO') and matricula.matricula = ingresso.aluno_id group by matricula.status,matricula.cidade order by Porcentagem desc")
    resultado = cursor.fetchall()
    html = render_template('cidadePdf.html', resultado=resultado)
    return render_pdf(HTML(string=html))

@app.route('/pdfingresso')
def pdfingresso():
    cursor.execute("SELECT matricula.status,ingresso.forma_ingresso, Round(count(matricula.status)/281*100,2) as Porcentagem FROM matricula,ingresso where(matricula.status like '%CONCLU%' or matricula.status like 'ABANDONO' or matricula.status like 'DESLIGADO') and matricula.matricula = ingresso.aluno_id group by matricula.status, ingresso.forma_ingresso order by Porcentagem desc")
    resultado = cursor.fetchall()
    html = render_template('ingressoPdf.html', resultado=resultado)
    return render_pdf(HTML(string=html))



@app.route('/pdfdisciplinas')
def pdfdisciplinas():
    resultado = cursor.execute("SELECT  * FROM disciplina group by nome order by periodo ")
    resultado = cursor.fetchall()
    html = render_template('disciplinasPdf.html', resultado=resultado)
    return render_pdf(HTML(string=html))

@app.route('/pdf')
def pdf():
    resultado =session['pdfAprovado']
    html = render_template('aprovacaoPdf.html', resultado=resultado)
    return render_pdf(HTML(string=html))

@app.route('/pdfAlunos')
def pdfAlunos():
    resultado = Alunos.query.filter(Alunos.resultado > 0).order_by(Alunos.nome)
    html = render_template('listagemAlunosPDF.html', resultado=resultado)
    return render_pdf(HTML(string=html))

@app.route('/pdfAlunosRiscos')
def pdfAlunosRiscos():
    resultado = Alunos.query.filter(Alunos.media >=60 ).order_by(Alunos.media.desc())
    html = render_template('listagemAlunosPDF.html', resultado=resultado)
    return render_pdf(HTML(string=html))

@app.route('/pdfAlunosRelatorios')
def pdfAlunosRelatorios():
    resultado = Alunos.query.filter(Alunos.id==session["a1"])
    disAlunos = Disciplinas_Alunos.query.filter(Disciplinas_Alunos.id_alunos==session["a1"])
    html = render_template('listagemAlunosDisciplinasPDF.html', resultado=resultado, disAlunos=disAlunos)
    return render_pdf(HTML(string=html))
