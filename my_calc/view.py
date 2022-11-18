from decimal import Decimal


def view_data(data):
    print(f'Результат = {data}')


def get_float_value():
    return Decimal(input('Введи число: '))


def get_complex_value():
    return complex(input('Введи число: '))


def get_action():
    return input('Доступные действия \n'
                 'Умножеие = *\n'
                 'Деление = /\n'
                 'Сложение = +\n'
                 'Вычитание = -\n'
                 'Введите действие = ')


def get_number_info():
    return int(input('Введи тип данных:\n'
                     'Комплексные = 1\n'
                     'Рациональные = 2\n'
                     'Выход из программы = 3: '))


def menu_error():
    print('Ошибка выбора меню')


def new_line():
    print()


mode = {'+': 'сумма', '-': 'разность', '*': 'произведение', '/': 'деление'}
info = {1: 'комплексные', 2: 'рациональные'}