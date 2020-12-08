from app import db
from werkzeug.security import generate_password_hash,check_password_hash

class User(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nome = db.Column(db.String)
    cpf = db.Column(db.String,unique=True)
    celular = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    nomeUsuario = db.Column(db.String, unique=True)
    tipo = db.Column(db.String)
    senha = db.Column(db.String)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __init__(self, nome,cpf, email,celular,nomeUsuario, tipo, senha):
        self.nome = nome
        self.cpf = cpf
        self.celular = celular
        self.email = email
        self.nomeUsuario = nomeUsuario
        self.tipo = tipo
        self.senha = senha

    def __repr__(self):
        return "<User %r>" % self.nome

class Periodo(db.Model):
    __tablename__ = "periodo"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.Text)

    def __init__(self, nome):
        self.nome = nome

    def __repr__(self):
        return "<Periodo %r>" % self.id

class Disciplina(db.Model):
            __tablename__ = "disciplina"
            id = db.Column(db.Integer, primary_key=True)
            nome = db.Column(db.Text)
            nomeData = db.Column(db.Text)
            equibsi = db.Column(db.Text)
            periodo = db.Column(db.Integer, db.ForeignKey('periodo.id'))
            Periodo = db.relationship('Periodo', foreign_keys=periodo)

            def __init__(self, nome, periodo,nomeData,equibsi):
                self.nome = nome
                self.periodo = periodo
                self.nomeData = nomeData
                self.equibsi = equibsi

            def __repr__(self):
                return "<Disciplina %r>" % self.id

class SituacaoDisciplinas(db.Model):
            __tablename__ = "situacaoDisciplinas"
            id = db.Column(db.Integer, primary_key=True)
            disciplina = db.Column(db.Text)
            situacaoDisciplina = db.Column(db.Text)
            data = db.Column(db.Text)
            periodo = db.Column(db.Integer, db.ForeignKey('periodo.id'))
            Periodo = db.relationship('Periodo', foreign_keys=periodo)

            def __init__(self,disciplina,situacaoDisciplina,data, periodo):
                self.disciplina = disciplina
                self.situacaoDisciplina = situacaoDisciplina
                self.data = data
                self.periodo = periodo

            def __repr__(self):
                return "<SituacaoDisciplina %r>" % self.id


class Alunos(db.Model):
    __tablename__ = "alunos"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    cpf = db.Column(db.Text)
    resultado = db.Column(db.Text)
    media = db.Column(db.Text)
    curso = db.Column(db.Text)


    def __init__(self,nome,cpf,resultado,media):
        self.nome = nome
        self.cpf = cpf
        self.resultado = resultado
        self.media = media

    def __repr__(self):
        return "<Alunos %r>" % self.id

class Disciplinas_Alunos(db.Model):
    __tablename__ = "disciplinas_alunos"

    id = db.Column(db.Integer, primary_key=True)
    id_disciplinas= db.Column(db.Text)
    id_alunos = db.Column(db.Text)
    nomeDisciplina = db.Column(db.Text)
    resultado = db.Column(db.Text)

    def __init__(self, id_disciplinas,nomeDisciplina,id_alunos,resultado):
        self.id_disciplinas = id_disciplinas
        self.id_alunos = id_alunos
        self.nomeDisciplina = nomeDisciplina
        self.resultado = resultado

    def __repr__(self):
        return "<Disciplina_Alunos %r>" % self.id
