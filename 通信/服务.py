import json
import os
import socket

import inside.Gui.Manage

NOT_FOUND = 'HTTP/1.1 404 NOT FOUND\n\n'.encode()
HTTP_OK = 'HTTP/1.1 200 OK\n\n'.encode()


def pages(path):
    if path == '/pages/GZTQ.html':
        inside.Gui.Manage.main()

    new_path = '前端{}'.format(path)
    if not os.path.isfile(new_path):
        return NOT_FOUND

    print('path: ({})'.format(new_path))
    with open(new_path, 'rb') as page:
        content = page.read()
        return HTTP_OK + content


def post(param):
    print('[post param] ({})'.format(param))

    param = json.loads(param)

    from 业务 import 词性标注, 语料管理
    comply = {
        'CXBZ': 词性标注.comply,
        'YLGL': 语料管理.comply,
    }

    return HTTP_OK + comply[param['pages']](param)


def routing(request, connection):
    req_type, path = request.split(b' ', 2)[:2]

    print('req_type: ({}), path: ({})'.format(req_type, path))
    if req_type == b'GET':
        return pages(path.decode())
    elif req_type == b'POST':
        head, body = request.split(b'\r\n\r\n', 1)
        if body == b'':
            body = b''
            while True:
                tem = connection.recv(1024)
                body += tem
                if len(tem) < 1024:
                    break
        return post(body)


def run(port=6187):
    print('请使用浏览器访问此链接进入【湘西苗文词性标注系统】：', 'http://localhost:{}/index.html'.format(port))

    with socket.socket() as s:
        s.bind(('', port))
        while True:
            s.listen(7)
            connection, address = s.accept()
            request = connection.recv(102400)

            # response = routing(request, connection)
            try:
                response = routing(request, connection)
            except Exception as e:
                print()
                print('[ERROR]\n({})\n({})'.format(e, request))
                print()
                continue

            connection.sendall(response)

            connection.close()


if __name__ == '__main__':
    run()
