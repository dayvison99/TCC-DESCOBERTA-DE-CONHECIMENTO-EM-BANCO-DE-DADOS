from app import db

class User(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nomeUsuario = db.Column(db.String, unique=True)
    senha = db.Column(db.String)
    nome = db.Column(db.String)
    celular = db.Column(db.Integer, unique=True)
    email = db.Column(db.String, unique=True)

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

    def __init__(self, nomeUsuario, senha, nome, celular, email):
        self.nomeUsuario = nomeUsuario
        self.senha = senha
        self.nome = nome
        self.celular = celular
        self.email = email

    def __repr__(self):
        return "<User %r>" % self.username

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
            periodo_id = db.Column(db.Integer, db.ForeignKey('periodo.id'))

            periodo = db.relationship('Periodo', foreign_keys=periodo_id)

            def __init__(self, nome, periodo_id):
                self.nome = nome
                self.periodo_id = periodo_id

            def __repr__(self):
                return "<Disciplina %r>" % self.id
