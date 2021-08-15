import json


def encode(data):
    if type(data) == dict:
        print('[tools encode]', data)
        return json.dumps(data).encode()
    return str(data).encode()
