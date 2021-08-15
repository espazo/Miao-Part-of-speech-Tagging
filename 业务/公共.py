import json


def finally_json(data, status=1, message='OK'):
    return {
        'status': status,
        'message': message,
        'data': data
    }
