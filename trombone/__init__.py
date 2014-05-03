# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Flask, request, render_template, send_from_directory, Markup, flash, redirect
from flask.ext.login import LoginManager, login_required, login_user, logout_user

from flask.ext import admin
from flask.ext.admin.contrib import sqla

import wtforms

from trombone.user import load_user
from trombone.models import db, User

class DefaultConfig(object):
    SECRET_KEY = 'Isthisthereallife?Isthisjustfantasy?Caughtinalandslide'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///./trombone.db'

app = Flask(__name__)
app.config.from_object('trombone.DefaultConfig')
#app.config.from_pyfile(self.config, silent=True)

# Configure the login manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = ".user.login"
login_manager.user_loader(load_user)

app.test_request_context().push()
db.init_app(app)
db.create_all()

# Create admin user if doesn't exist
admin_user = User.query.get(1)
if not admin_user:
    admin_user = User("admin", "admin", is_admin=True)
    db.session.add(admin_user)
    db.session.commit()

class UserAdmin(sqla.ModelView):
    pass

admin = admin.Admin(app, 'Trombone')
admin.add_view(UserAdmin(User, db.session))

# Start the application
app.run(port=8000)

