from random import choice

def raspredelitel(input_list: list) -> list | None:
    """
    task:
    Задать 90-элементный ранжовый список. Выделить из него 18 неповторяющихся групп,
    по 5 уникальных номеров-элементов (из первого списка) в каждой и вывести.

    :param input_list:
    :return: list or None
    """
    if len(input_list) != 90:
        print("count obj != 90")
        return None
    if len(set(input_list)) != 90:
        print("some obj repeated, count obj != 90, then del all repeats")
        return None

    new_list = []

    for _ in range(18):
        list_subj = []
        for _ in range(5):
            obj = (choice(input_list))
            list_subj.append(obj)

        new_list.append(list_subj)

    return new_list
