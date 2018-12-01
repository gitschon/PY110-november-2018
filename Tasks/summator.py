"""
Данный модуль предоставляет вам возможность складывать суммировать массивы и находить их
среднее арифметическое.
"""

class SummatorError(Exception):
    """
    Класс необходимый для создания собственных исключений.
    """
    pass


def is_inp_correct(l):
    """
    Функция производит проверку на корректность ввода

    :param l:
    :return:
    """
    for i in l:
        if type(i) != int and type(i) != float:
            return False
    return True


def my_sumf(input):
    """

    :param input:
    :return:
    """
    if not is_inp_correct(input):
        raise SummatorError("На вход был подан массив с некорректными данными")
    my_sum = 0
    for i in input:
        my_sum += i
    return my_sum


def avg(input):
    """

    :param input:
    :return:
    """
    if len(input) == 0:
        raise SummatorError("На вход был подан пустой массив")
    if not is_inp_correct(input):
        raise SummatorError("На вход был подан массив с некорректными данными")

    my_avg = my_sumf(input) / len(input)

    return my_avg


if __name__ == '__main__':
    pass