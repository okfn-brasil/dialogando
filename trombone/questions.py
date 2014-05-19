from flask import request, flash, redirect, render_template
from models import Person, SimpleQuestion, SimpleAnswers, db

def questions_page(question_id):
    person_slug = request.args.get('u')
    u = Person.query.filter(Person.slug == person_slug).all()[0]

    if u:
        # Get questions
        question = SimpleQuestion.query.filter(SimpleQuestion.id == question_id).all()[0]
        answer = SimpleAnswers.query.filter(SimpleAnswers.person_id == u.id and SimpleAnswers.question_id == question_id).all()[0]

        if answer:
            form = question.create_form(request, answer)
        else:
            form = question.create_form(request)

        if request.method == 'GET':
            return render_template("question.html", question=question, form=form, person_slug=person_slug)
        elif request.method == 'POST' and form.validate():
            add_answer = False
            if not answer:
                new_answer = SimpleAnswers()
                add_answer = True
            else:
                new_answer = answer

            new_answer.person = u
            new_answer.dissertative_1 = form['dissertative_1'].data
            new_answer.dissertative_2 = form['dissertative_2'].data
            new_answer.alternative = form['alternative'].data
            new_answer.simple_question_id = question_id

            if add_answer:
                db.session.add(new_answer)
            db.session.commit()

            return render_template("question.html", question=question, form=form, person_slug=person_slug)

    return redirect('/')
