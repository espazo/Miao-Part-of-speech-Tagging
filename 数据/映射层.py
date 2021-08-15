def ku_file(name):
    file_name = name
    data = {}

    def init():
        nonlocal data

        with open('数据/库/' + name, 'r', encoding='utf-8') as file:
            raw = file.read().strip()
            for r in raw.split():
                k, v = r.split('/')
                data[k] = v

    def update():
        with open('数据/库/' + name, 'w', encoding='utf-8') as file:
            for k, v in data.items():
                file.write(k + '/' + v + '\t')

    def get_data():
        return data

    def set_data(dicts):
        nonlocal data
        data = dicts

    init()

    return {
        'update': update,
        'data': get_data,
        'name': file_name,
        'set_data': set_data,
    }
