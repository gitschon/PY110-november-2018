"""
Данный модуль производит импорт улиц из json(файл или строка),
генерирует и выдаёт случайные адреса на основе этого списка по одному.
"""
import json
import re
import random as rnd


class MyError(Exception):
    """
    Класс необходимый для создания собственных исключений.
    """
    pass


def file_create(file_name):
    """
    Данная функция создаёт файл со строкой json.
    :param file_name:Имя файла.
    :return:
    """
    my_dict = {
        "1": ["РФ", "СПБ", "Восстания"],
        "2": ["РФ", "СПБ", "Жуковского"],
        "3": ["РФ", "СПБ", "Маяковского"],
        "4": ["РФ", "СПБ", "Есенина"]
    }

    with open(file_name, 'w', encoding='utf8') as f:
        json.dump(my_dict, f)
    return print(f"Файл {file_name} создан.")


def test_decorator(func):
    """
    Данная функция декорирует передаваемую функцию, если встречает строку "test" в параметрах,
    выводит сообщение вместо запуска декорируемой функции.
    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        t_word = 'test'
        if args:
            if t_word in args:
                return f'Вызов функции {func.__name__} с параметрами {args}'
        elif kwargs:
            for par in kwargs.values():
                if t_word == par:
                    return f'Вызов функции {func.__name__} с параметрами {tuple(kwargs)}'
        else:
            return func(*args, **kwargs)
        return None
    return wrapper


def is_adr_correct(my_dict):
    """
    Данная функция проверяет на корректность исходный список улиц.
    :param my_dict:
    :return:True - если данные корректны, False в противном случае.
    """
    for adr in my_dict.values():
        flag = re.search(r'^\w{2,}$', adr[-1])
        if not flag:
            return False
        else:
            return True
    return None


def import_adr_string(json_string=""):
    """
    Данная функция производит импорт json строки переданной ей на вход.
    :param json_string:Строка формата json
    :return:Словарь с импортированными данными.
    """
    my_dict = json.loads(json_string)
    if not is_adr_correct(my_dict):
        raise MyError("На вход подана строка с адресами содержащая ошибки")
    return my_dict


def import_adr_file(json_file=""):
    """
    Данная функция производит импорт json строки из переданного ей файла.
    :param json_file: Полное имя файла
    :return: Словарь с импортированными данными.
    """
    with open(json_file, encoding='utf-8') as jf:
        data = jf.readline()
    my_dict = json.loads(data)
    if not is_adr_correct(my_dict):
        raise MyError("На вход подан файл с адресами содержащий ошибки")
    return my_dict


def adr_generator(j_string="", j_file=""):
    """
    Данная функция - генератор случайных почтовых адресов.
    :param j_string: Строка json.
    :param j_file: Полное имя файла со строкой json.
    :return: Печатает строку сгенерированного адреса.
    """
    if j_file:
        my_dict = import_adr_file(json_file=j_file)
    elif j_string:
        my_dict = import_adr_string(json_string=j_string)
    else:
        raise MyError("Генератор должен быть вызван с одним из параметров")
    while True:
        for adr in my_dict.values():
            yield print(f'{" ".join(adr)} дом {rnd.randint(1,100)} квартира {rnd.randint(1,300)}')


if __name__ == '__main__':
    file_create('..\\json_file.txt')
