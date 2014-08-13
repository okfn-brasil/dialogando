# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Flask, request, render_template, send_from_directory, Markup, flash, redirect
from flask.ext.login import LoginManager, login_required, login_user, logout_user
#from flask.ext import login

import wtforms

import trombone.user as user
import trombone.main as main
import trombone.questions as questions
from trombone.models import *
from trombone.admin import admin

class DefaultConfig(object):
    SECRET_KEY = 'Isthisthereallife?Isthisjustfantasy?Caughtinalandslide'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./trombone.db'
    PROPAGATE_EXCEPTIONS = True

app = Flask(__name__)
app.config.from_object('trombone.DefaultConfig')
#app.config.from_pyfile(self.config, silent=True)

# Configure the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ".user.login"
login_manager.user_loader(user.load_user)

app.test_request_context().push()
db.init_app(app)
db.create_all()

# Create admin user if doesn't exist
admin_user = User.query.get(1)
if not admin_user:
    admin_user = User("admin", "admin", is_admin=True)
    db.session.add(admin_user)
    db.session.commit()

# Create admin interface
admin.init_app(app)

# Add routes

# Root page
app.add_url_rule("/", "soon", main.root, methods=['GET'])
app.add_url_rule("/p", "root", main.main, methods=['GET'])

# Answers page
app.add_url_rule("/respostas", "answers", main.answers, methods=['GET'])

# Admin interface
app.add_url_rule("/login", "login", user.login, methods=['POST', 'GET'])
app.add_url_rule("/logout", "logout", user.logout, methods=['POST', 'GET'])

# Questions list
app.add_url_rule("/responder/<int:question_id>", "responder", questions.questions_page, methods=['GET', 'POST'])

# Start the application
app.run(host='0.0.0.0', port=5001)
