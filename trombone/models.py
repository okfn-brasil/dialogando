# -*- coding: utf-8 -*-

import sha
import wtforms
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

class SimpleQuestion(db.Model):
    __tablename__ = 'simple_questions'
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.Integer, db.ForeignKey('questions_topics.id'))
    title =  db.Column(db.Text)
    description = db.Column(db.Text)
    dissertative_1 =  db.Column(db.Text)
    dissertative_2 = db.Column(db.Text)
    alternative_a = db.Column(db.Text)
    alternative_b = db.Column(db.Text)
    back_question_id = db.Column(db.Integer)
    next_question_id = db.Column(db.Integer)

    def create_form(self, request, data=None):
        class QuestionForm(wtforms.Form):
            dissertative_1 = wtforms.TextAreaField(self.dissertative_1)
            dissertative_2 = wtforms.TextAreaField(self.dissertative_2)
            alternative = wtforms.RadioField(default='3', choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')])
            go_back = wtforms.HiddenField("go_back")

        form = QuestionForm(request.form, data) if data else  QuestionForm(request.form)

        return form

class Topic(db.Model):
    __tablename__ = 'questions_topics'
    id = db.Column(db.Integer, primary_key=True)
    title =  db.Column(db.Text)
    description = db.Column(db.Text)
    simple_question = db.relationship(SimpleQuestion)

class SimpleAnswers(db.Model):
    __tablename__ = 'simple_answers'
    id = db.Column(db.Integer, primary_key=True)
    dissertative_1 =  db.Column(db.Text)
    dissertative_2 = db.Column(db.Text)
    alternative = db.Column(db.Text)
    simple_question_id = db.Column(db.Integer, db.ForeignKey('simple_questions.id'))
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'))

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
    answers = db.relationship('AlternativeOption', backref='question')

class AlternativeOption(db.Model):
    __tablename__ = 'alternative_options'
    id = db.Column(db.Integer, primary_key=True)
    alt_question_id = db.Column(db.Integer, db.ForeignKey('alternative_questions.id'))
    option = db.Column(db.Text)
    position = db.Column(db.Integer)

class Person(db.Model):
    __tablename__ = 'person'
    id = db.Column(db.Integer, primary_key=True)
    slug = db.Column(db.Text)
    name = db.Column(db.Text)
    email = db.Column(db.Text)
    website = db.Column(db.Text)
    info = db.Column(db.Text)
    party = db.Column(db.Text)
    sex = db.Column(db.Text)
    candidature = db.Column(db.Text)
    answers = db.relationship('SimpleAnswers', backref='person')

class PersonDissertativeAnswer(db.Model):
    __tablename__ = 'person_dissertative_answer'
    id = db.Column(db.Integer, primary_key=True)
    dissertative_question_id = db.Column(db.Integer, db.ForeignKey('dissertative_questions.id'))
    answer = db.Column(db.Text)

class PersonAlternativeAnswer(db.Model):
    __tablename__ = 'person_alternative_answer'
    id = db.Column(db.Integer, primary_key=True)
    alternative_option_id = db.Column(db.Integer, db.ForeignKey('alternative_options.id'))
    answer = db.Column(db.Integer, db.ForeignKey('alternative_options.id'))

