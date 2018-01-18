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

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    user = db.relationship('User', foreign_keys=user_id)

    def __init__(self, content, user_id):
        self.content = content
        self.user_id = user_id

    def __repr__(self):
        return "<Post %r>" % self.id

class Follow(db.Model):
    __tablename__ = "follow"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))
    follower_id = db.Column(db.Integer, db.ForeignKey('usuario.id'))

    user = db.relationship('User', foreign_keys=user_id)
    follower = db.relationship('User', foreign_keys=follower_id)
