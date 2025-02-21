"""
Задана матрица из 3-х списков: Сначала разбить матрицу вертикально,
5 колонок-столбцов слева, остальные справа.
Красиво вывести две части матрицы, чтоб по одной высоте: левая часть слева,
правая справа. Далее создать 8 именованных
кортежей: lfi5, lfi4, lfi3, lfi2, rfi2, rfi3, rfi4, rfi5

Задача в том, чтоб в бесконеч. цикле юзер жал, например, rfi3, а
выводится соответствуючий столбец или столбцы. Максимальная автоматизация-
алгоритмизация приветствуется!! Конец икла при нулёвом вводе!!
"""
from collections import namedtuple
def num_12():
    # Исходная матрица
    matrix = [
        ['16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '43'],
        ['30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '00', '00'],
        ['44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '00', '00', '00']
    ]

    # Разделяем матрицу на левую и правую части
    left_part = [[row[:5] for row in matrix]]
    right_part = [[row[5:] for row in matrix]]

    # Красивый вывод левой и правой частей
    max_height = max(len(left_part[0]), len(right_part[0]))

    # Выводим обе части
    for i in range(max_height):
        left_row = left_part[0][i] if i < len(left_part[0]) else [''] * 5
        right_row = right_part[0][i] if i < len(right_part[0]) else [''] * (len(matrix[0]) - 5)
        print(' | '.join(left_row).ljust(30) + '| ' + ' | '.join(right_row))

    # Создаем именованные кортежи
    LFI = namedtuple('LFI', ['lfi5', 'lfi4', 'lfi3', 'lfi2'])
    RFI = namedtuple('RFI', ['rfi2', 'rfi3', 'rfi4', 'rfi5'])

    lfi5 = tuple(row[0] for row in matrix)
    lfi4 = tuple(row[1] for row in matrix)
    lfi3 = tuple(row[2] for row in matrix)
    lfi2 = (matrix[0][3], matrix[0][4])  # Столбцы 19 и 20

    rfi2 = (matrix[0][5], matrix[0][6])  # Столбцы 21 и 22
    rfi3 = tuple(row[7] for row in matrix)
    rfi4 = tuple(row[8] for row in matrix)
    rfi5 = tuple(row[9] for row in matrix)

    # Создаем кортежи
    left_tuples = LFI(lfi5=lfi5, lfi4=lfi4, lfi3=lfi3, lfi2=lfi2)
    right_tuples = RFI(rfi2=rfi2, rfi3=rfi3, rfi4=rfi4, rfi5=rfi5)

    # Бесконечный цикл для ввода пользователя
    while True:
        user_input = input("Введите имя кортежа (например, lfi3 или rfi2) или 0 для выхода: ")
        if user_input == "0":
            break
        elif hasattr(left_tuples, user_input):
            print(getattr(left_tuples, user_input))
        elif hasattr(right_tuples, user_input):
            print(getattr(right_tuples, user_input))
        else:
            print("Некорректный ввод. Попробуйте снова.")

if __name__ == '__main__':
    num_12()