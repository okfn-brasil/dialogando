from flask import redirect
from flask.ext import admin
from flask.ext.admin import expose
from flask.ext.admin.contrib import sqla
from flask.ext import login

from trombone.models import *

# Create customized index view class that handles login & registration
class MyAdminIndexView(admin.AdminIndexView):

    @expose('/')
    def index(self):
        if not login.current_user.is_authenticated():
            return redirect('/login')
        return super(MyAdminIndexView, self).index()

class UserAdmin(sqla.ModelView):
    def is_accessible(self):
        return login.current_user.is_authenticated()

class AlternativeQuestionAdmin(sqla.ModelView):
    inline_models = (AlternativeOption,)

    def is_accessible(self):
        return login.current_user.is_authenticated()

class ThemeQuestionAdmin(sqla.ModelView):
    inline_models = (DissertativeQuestion,)

    def is_accessible(self):
        return login.current_user.is_authenticated()

class SimpleQuestionAdmin(sqla.ModelView):
#    inline_models = (SimpleQuestion,)

    def is_accessible(self):
        return login.current_user.is_authenticated()

class SimpleAnswersAdmin(sqla.ModelView):
    inline_models = (Person, )

    def is_accessible(self):
        return login.current_user.is_authenticated()

class PersonAdmin(sqla.ModelView):
#    inline_models = (SimpleQuestion,)
    column_searchable_list = ('name',)

    def is_accessible(self):
        return login.current_user.is_authenticated()


admin = admin.Admin(name='Trombone', index_view=MyAdminIndexView(), base_template='my_master.html')
admin.add_view(UserAdmin(User, db.session))
#admin.add_view(ThemeQuestionAdmin(ThemeQuestions, db.session))
admin.add_view(SimpleQuestionAdmin(SimpleQuestion, db.session))
admin.add_view(SimpleAnswersAdmin(SimpleAnswers, db.session))
admin.add_view(PersonAdmin(Person, db.session))
#admin.add_view(AlternativeQuestionAdmin(AlternativeQuestion, db.session))


