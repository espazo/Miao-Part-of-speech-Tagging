import json
import os
from 业务.公共 import finally_json
from 工具.工具 import encode
from 数据.映射层 import ku_file


def comply(data):
    dicts = {
        'init': file_list,
        'file': file_data,
        'save': file_save,
        'remove': file_remove,
        'upload': file_upload,
    }
    return dicts[data['model']](data['data'])


def file_list(data):
    files = os.listdir('数据/库/')
    return encode(finally_json(files))


def file_data(data):
    with open('数据/库/' + data, 'r', encoding='utf-8') as file:
        return encode(finally_json(file.read()))


def file_save(data):
    dicts = {}

    data = json.loads(data)
    try:
        print('[file_save]', data, data['data'].split())
        for d in data['data'].split():
            k, v = d.split('/')
            dicts[k] = v
    except Exception as e:
        return encode(finally_json(None, 0, '文件格式有误！'))

    file = ku_file(data['name'])
    file['set_data'](dicts)
    file['update']()

    if 'new_name' in data and data['new_name'] != data['name']:
        os.rename('数据/库/' + data['name'], '数据/库/' + data['new_name'])

    return encode(finally_json(None))


def file_remove(data):
    try:
        os.remove('数据/库/' + data)
    except Exception as e:
        return encode(finally_json(None, 0, '文件删除失败。'))

    return encode(finally_json(None))


def file_upload(data):
    data = json.loads(data)
    file_path = '数据/库/' + data['name']

    if os.path.exists(file_path):
        return encode(finally_json(None, 0, '文件已存在。'))

    with open(file_path, 'w') as file:
        pass

    message = file_save(json.dumps(data))
    if message != encode(finally_json(None)):
        file_remove(data['name'])
        return message

    return encode(finally_json(None))


if __name__ == '__main__':
    print(os.listdir('../数据/库/'))
    os.chdir('../')
    print(os.getcwd())
    file_remove('HELLO.txt')
