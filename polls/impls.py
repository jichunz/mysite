from datetime import datetime

from .models import Question, Choice


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


def update_question(question_id, question_text):
    question = Question.objects.get(id=question_id)
    question.question_text = question_text
    question.pub_date = datetime.now()
    question.save()
    return dict(id=question.id, question_text=question.question_text, pub_date=question.pub_date)


def delete_question(question_id):
    question = Question.objects.get(id=question_id)
    question.delete()
    return dict(id=question_id)


def get_choices(question_id):
    question = Question.objects.get(id=question_id)
    choices = Choice.objects.filter(question=question)
    return dict(question_id=question_id, question_text=question.question_text, question_pub_date=question.pub_date,
                choices=[dict(id=c.id, choice_text=c.choice_text, votes=c.votes) for c in choices])


def get_choice(choice_id):
    choice = Choice.objects.get(id=choice_id)
    return dict(question_id=choice.question.id, question_text=choice.question.question_text,
                question_pub_date=choice.question.pub_date, choice_id=choice.id, choice_text=choice.choice_text,
                choice_votes=choice.votes)


def create_choice(question_id, choice_text, votes):
    question = Question.objects.get(id=question_id)
    choice = Choice.objects.create(question=question, choice_text=choice_text, votes=votes if votes else 0)
    return dict(question_id=question_id, question_text=question.question_text, choice_id=choice.id,
                choice_text=choice_text, votes=choice.votes)


def update_choice(choice_id, choice_text, votes):
    choice = Choice.objects.get(id=choice_id)
    choice.choice_text = choice_text
    if votes:
        choice.votes = votes
    choice.save()
    return dict(question_id=choice.question.id, question_text=choice.question.question_text, choice_id=choice.id,
                choice_text=choice_text, votes=choice.votes)


def delete_choice(choice_id):
    choice = Choice.objects.get(id=choice_id)
    choice.delete()
    return dict(id=choice_id)
