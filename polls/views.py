import json

from django.http import JsonResponse
from jsonschema import validate

from util import create_response, error_response
from . import impls


# Create your views here.


def questions(request):
    if request.method != 'GET':
        return JsonResponse(dict(status=500, message='Request method not supported.'))
    return create_response(impls.get_questions())


def question(request):
    if request.method == 'GET':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "question_id": {
                    "type": "string",
                    "pattern": "[1-9][0-9]*"
                }
            },
            "required": [
                "question_id",
            ]
        }

        body = request.GET
        try:
            validate(json.loads(json.dumps(body)), schema)
            result = impls.get_question(question_id=int(body.get('question_id')))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    elif request.method == 'POST':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "question_text": {
                    "type": "string"
                }
            },
            "required": [
                "question_text",
            ]
        }

        body = json.loads(request.body)
        try:
            validate(body, schema)
            result = impls.create_question(question_text=body.get('question_text'))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    elif request.method == 'PUT':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "question_id": {
                    "type": "integer"
                },
                "question_text": {
                    "type": "string"
                }
            },
            "required": [
                "question_id",
                "question_text",
            ]
        }

        body = json.loads(request.body)
        try:
            validate(body, schema)
            result = impls.update_question(question_id=body.get('question_id'),
                                           question_text=body.get('question_text'))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    elif request.method == 'DELETE':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "question_id": {
                    "type": "string",
                    "pattern": "[1-9][0-9]*"
                }
            },
            "required": [
                "question_id",
            ]
        }

        body = request.GET
        try:
            validate(json.loads(json.dumps(body)), schema)
            result = impls.delete_question(question_id=int(body.get('question_id')))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    else:
        return error_response(Exception(message='Request method not supported'))


def choices(request):
    if request.method != 'GET':
        return JsonResponse(dict(status=500, message='Request method not supported.'))
    schema = {
        "$schema": "http://json-schema.org/draft-04/schema#",
        "type": "object",
        "properties": {
            "question_id": {
                "type": "string",
                "pattern": "[1-9][0-9]*"
            }
        },
        "required": [
            "question_id",
        ]
    }

    body = request.GET
    try:
        validate(json.loads(json.dumps(body)), schema)
        result = impls.get_choices(question_id=int(body.get('question_id')))
        return create_response(result)
    except Exception as e:
        return error_response(e)


def choice(request):
    if request.method == 'GET':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "choice_id": {
                    "type": "string",
                    "pattern": "[1-9][0-9]*"
                }
            },
            "required": [
                "choice_id",
            ]
        }

        body = request.GET
        try:
            validate(json.loads(json.dumps(body)), schema)
            result = impls.get_choice(choice_id=int(body.get('choice_id')))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    elif request.method == 'POST':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "question_id": {
                    "type": "integer"
                },
                "choice_text": {
                    "type": "string"
                },
                "votes": {
                    "type": "integer"
                }
            },
            "required": [
                "question_id",
                "choice_text"
            ]
        }

        body = json.loads(request.body)
        try:
            validate(body, schema)
            result = impls.create_choice(question_id=body.get('question_id'), choice_text=body.get('choice_text'),
                                         votes=body.get('votes'))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    elif request.method == 'PUT':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "choice_id": {
                    "type": "integer"
                },
                "choice_text": {
                    "type": "string"
                },
                "votes": {
                    "type": "string"
                }
            },
            "required": [
                "choice_id",
                "choice_text",
            ]
        }

        body = json.loads(request.body)
        try:
            validate(body, schema)
            result = impls.update_choice(choice_id=body.get('choice_id'), choice_text=body.get('choice_text'),
                                         votes=body.get('votes'))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    elif request.method == 'DELETE':
        schema = {
            "$schema": "http://json-schema.org/draft-04/schema#",
            "type": "object",
            "properties": {
                "choice_id": {
                    "type": "string",
                    "pattern": "[1-9][0-9]*"
                }
            },
            "required": [
                "choice_id",
            ]
        }

        body = request.GET
        try:
            validate(json.loads(json.dumps(body)), schema)
            result = impls.delete_choice(choice_id=int(body.get('choice_id')))
            return create_response(result)
        except Exception as e:
            return error_response(e)
    else:
        return error_response(Exception(message='Request method not supported'))
