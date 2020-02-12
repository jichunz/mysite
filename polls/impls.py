from datetime import datetime

from .models import Question


def get_questions():
    questions = Question.objects.all()
    return dict(questions=[dict(id=q.id,
                                question_text=q.question_text,
                                pub_date=q.pub_date) for q in questions])


def get_question(question_id):
    question = Question.objects.get(id=question_id)
    return dict(id=question.id, question_text=question.question_text, pub_date=question.pub_date)


def create_question(question_text):
    question = Question.objects.create(question_text=question_text, pub_date=datetime.now())
    return dict(id=question.id, question_text=question_text, pub_date=question.pub_date)
