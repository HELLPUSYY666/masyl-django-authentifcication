from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def core_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response = {
            'error': {
                'status_code': response.status_code,
                'message': response.data
            }
        }
        response.data = custom_response
    else:
        custom_response = {
            'error': {
                'status_code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                'message': 'Внутренняя ошибка сервера.'
            }
        }
        return Response(custom_response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
