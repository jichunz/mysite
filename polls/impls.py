from datetime import datetime

from .models import Question, Choice


def get_questions():
    rows = Question.objects.all().values('id',
                                         'question_text',
                                         'pub_date',
                                         'choice__id',
                                         'choice__choice_text',
                                         'choice__votes')
    result = dict()
    for row in rows:
        question_id = row.get('id')
        question = result.get(question_id)
        if not question:
            question = dict(question_id=question_id, question_text=row.get('question_text'),
                            question_pub_date=row.get('pub_date'))
            result[question_id] = question
        choices = question.get('choices')
        if not choices:
            choices = list()
            question['choices'] = choices
        choices.append(dict(choice_id=row.get('choice__id'), choice_text=row.get('choice__choice_text'),
                            votes=row.get('choice__votes')))
    return dict(questions=list(result.values()))


def get_question(question_id):
    rows = Question.objects.filter(id=question_id).values('id',
                                                          'question_text',
                                                          'pub_date',
                                                          'choice__id',
                                                          'choice__choice_text',
                                                          'choice__votes')
    choices = list()
    for row in rows:
        question_text = row.get('question_text')
        pub_date = row.get('pub_date')
        choice_id = row.get('choice__id')
        if choice_id:
            choices.append(dict(choice_id=choice_id, choice_text=row.get('choice__choice_text'),
                                votes=row.get('choice__votes')))
    return dict(question_id=question_id, question_text=question_text, pub_date=pub_date, choices=choices)


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
