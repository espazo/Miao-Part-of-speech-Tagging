from 数据.映射层 import ku_file


def dao():
    files = []

    def get_file(name):
        for f in files:
            if name == files['name']:
                return f
        return set_file(name)

    def set_file(name):
        file = ku_file(name)
        files.append(file)
        return file

    return {
        'get_file': get_file
    }
