"""
    task:
    Задать 90-элементный ранжовый список. Выделить из него 18 неповторяющихся групп,
    по 5 уникальных номеров-элементов (из первого списка) в каждой и вывести.

    :param input_list:
    :return: list or None
"""

from random import choice, shuffle, sample


def gen_list_rand_int_unic(start: int = 1, end: int = 91) -> list:
    rn = [x for x in range(start, end)]
    shuffle(rn)
    return rn


def sec_var(in_l: list, count_g: int, count_v: int = 5):
    if len(in_l) % count_g != 0:
        return []
    # else:
    #    if count_v == None:
    #            count_v = int(len(in_l) / count_g)

    res_val = []
    for _ in range(count_g):
        group_val = []
        group_val = sample(in_l, k=count_v)
        res_val.append(group_val)
        for ob in group_val:
            in_l.remove(ob)

    return res_val


def raspredelitel(input_list: list, count_groups: int, count_vals: int = 5) -> list:
    if len(input_list) % count_groups != 0:
        return []
    else:
        count_vals = int(len(input_list) / count_groups)
    new_list = []

    for _ in range(count_groups):
        list_subj = []
        for _ in range(count_vals):
            obj = choice(input_list)
            del input_list[input_list.index(obj)]
            list_subj.append(obj)

        new_list.append(list_subj)

    return new_list


if __name__ == "__main__":
    list_ob = gen_list_rand_int_unic()

    # for ob in raspredelitel(input_list=list_ob,count_groups=18, count_vals=5):
    #    print(ob)

    for ob in sec_var(in_l=list_ob, count_g=18, count_v=5):
        print(ob)
