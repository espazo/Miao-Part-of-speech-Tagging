import json
import joblib


def ta():
    data = None
    file_path = r'C:\Users\Julius\Desktop\湘西苗文词性标注\已标注语料整理\figure\utf_8编码\龙山苗语例句.dict'
    file_path = r'C:\Users\Julius\Desktop\湘西苗文词性标注\已标注语料整理\figure\utf_16_le编码\曾虎.dict'
    with open(file_path, 'rb') as file:
        data = joblib.load(file)

    print(data)
    print(type(data))


def tb():
    file_path = '数据/库/2019苗文.txt'
    with open(file_path, 'rb') as file:
        raw_text = file.read()
        # print(raw_text.split())
        raw_text = [i.split(b'/') for i in raw_text.split()]
        for i in raw_text:
            print(i)


def tc():
    from 数据.映射层 import ku_file
    hello = ku_file('HELLO.txt')
    print(hello['data']())
    hello['data']()['打开'] = 'hello'
    dicts = {'1': '2', '3': '4'}
    hello['set_data'](dicts)
    print(hello['data']())
    hello['update']()


def td():
    with open('数据/库/吉卫苗语2.txt', 'r', encoding='utf-8') as file:
        lst = file.read().split()

        # with open('数据/库/吉卫苗语2.txt', 'w', encoding='utf-8') as write:
        #     for i in range(len(lst)):
        #         write.write(lst[i])
        #         if '/' in lst[i]:
        #             write.write('\n')
        #         else:
        #             write.write("'")

        for i in range(len(lst)):
            if len(lst[i].split('/')) != 2:
                print(i + 1, end='\t')


if __name__ == '__main__':
    ta()
