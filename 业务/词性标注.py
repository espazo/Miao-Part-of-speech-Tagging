import json
import os

from 业务.公共 import finally_json
from 工具.工具 import encode
import thulac


def comply(data):
    dicts = {
        'save': save,
        0: chinese,
        1: miao,
    }
    return dicts[data['model']](data['data'])


def chinese(data):
    thu = thulac.thulac()
    res = thu.cut(data)
    return encode(finally_json(res))


def miao(data):
    file_path = '数据/库/'
    names = os.listdir(file_path)

    dicts = {}
    from 数据.映射层 import ku_file
    for name in names:
        file = ku_file(name)['data']()
        dicts.update(file)

    thu = thulac.thulac()
    res = thu.cut(data)
    for i in range(len(res)):
        k, _ = res[i]
        if k in dicts:
            res[i][1] = dicts[k]

    return encode(finally_json(res))


def save(data):
    from 业务.语料管理 import file_upload
    return file_upload(data)


if __name__ == '__main__':
    os.chdir('../')
    print(os.getcwd())
    miao(None)

