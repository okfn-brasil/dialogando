import sha
from flask.ext.sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self, username, password, email='', is_admin=False):
        self.username = username
        self.password = sha.new(password).hexdigest()
        self.email = email
        self.is_admin = is_admin

    def __repr__(self):
        return '<User %r>' % self.username

    def is_active(self):
        return True

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

class ThemeQuestions(db.Model):
    __tablename__ = 'theme_questions'
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.Text)
    dissertative = db.relationship('DissertativeQuestion', backref='theme')
    alternative  = db.relationship('AlternativeQuestion', backref='theme')

class DissertativeQuestion(db.Model):
    __tablename__ = 'dissertative_questions'
    id = db.Column(db.Integer, primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey('theme_questions.id'))
    question = db.Column(db.Text)
    position = db.Column(db.Integer)

class AlternativeQuestion(db.Model):
    __tablename__ = 'alternative_questions'
    id = db.Column(db.Integer, primary_key=True)
    theme_id = db.Column(db.Integer, db.ForeignKey('theme_questions.id'))
    question = db.Column(db.Text)
    position = db.Column(db.Integer)

