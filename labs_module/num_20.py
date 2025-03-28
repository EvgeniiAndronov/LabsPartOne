"""
Через списковое включение вывести все четные числа в диапазоне -150, до 150 с шагом 5,
включая крайние точки, при этом профильтровать, чтобы не выводились кратные 20,
также вывести сколько их получилось таких чисел?
:return: count type int
"""


def num_20(*args, krat=20) -> list:
    even_numbers = [
        x for x in range(args[0], args[1], args[2]) if x % 2 == 0 and x % krat != 0
    ]
    return even_numbers


if __name__ == "__main__":
    print("count elements - ", len(num_20(-150, 150, 5)))
    print("elements - ", *num_20(-150, 150, 5))
