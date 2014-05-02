# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from flask import Flask, request, render_template, send_from_directory, Markup, flash, redirect
from flask.ext.login import LoginManager, login_required, login_user, logout_user
import wtforms

class DefaultConfig(object):
    SECRET_KEY = 'Isthisthereallife?Isthisjustfantasy?Caughtinalandslide'
    SQLALCHEMY_DATABASE_URI = 'sqlite:////tmp/formcreator.db'


app = Flask(__name__)
app.config.from_object('trombone.DefaultConfig')
#app.config.from_pyfile(self.config, silent=True)
app.run()

