from flask import request, flash, redirect, render_template
from flask.ext.login import login_required, login_user, logout_user
import wtforms

from trombone.models import User

import sha

def logout(self):
    logout_user()
    return redirect("/")

def login(self):
    login_form = wtforms.form.BaseForm(())
    login_form['username'] = wtforms.TextField("Username")
    login_form['password'] = wtforms.PasswordField("Password")
    login_form['username'].data = ''

    if request.method == 'POST':
        login_form.process(request.form)
        if login_form.validate():
            # login and validate the user...
            password = sha.new(login_form['password'].data).hexdigest()
            u = User.query.filter(User.username == login_form['username'].data,
                                  User.password == password).all()
            if u:
                login_user(u[0])
                flash("Logged in successfully.")
                return redirect(request.args.get("next") or "/")
            else:
                flash("Username or password incorrect, try again.")

        return redirect("/login")

    return render_template("login.html", form=login_form, app=self)

def load_user(self, userid):
   return User.query.get(userid)


