from django.http import JsonResponse


def create_response(data):
    return JsonResponse(status=200, data=data)


def error_response(e):
    return JsonResponse(status=e.code if hasattr(e, 'code') else '500',
                        data=dict(error_message=e.message if hasattr(e, 'message') else str(e)))
