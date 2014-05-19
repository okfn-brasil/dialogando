from flask import request, flash, redirect, render_template
from models import Person, SimpleQuestion

def questions_page(question_id):
    person_slug = request.args.get('u')
    u = Person.query.filter(Person.slug == person_slug).all()

    if u:
        # Grab questions
        question = SimpleQuestion.query.filter(SimpleQuestion.id == question_id).all()[0]
        form = question.create_form(request)

        print form

        # Grab person's answers information
        return render_template("question.html", question=question, form=form, person_slug=person_slug)

    return redirect('/')
