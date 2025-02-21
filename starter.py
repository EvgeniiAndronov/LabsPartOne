from random import randint, shuffle, random

from labs_module.num_11 import raspredelitel
from labs_module.num_6 import b2int
from labs_module.num_20 import num_20
from labs_module.num_68 import draw_rectangle
from labs_module.num_12 import num_12

def gen_list_width_height_rand(count: int, min_val: int = 2, max_val: int = 10) -> list:
    result: list = []
    for _ in range(count):
        for _ in range(2):
            result.append([randint(min_val, max_val), randint(min_val, max_val)])

    return result

def gen_list_rand_int_unic(start: int = 1, end: int = 91) -> list:
    rn = [x for x in range(start, end)]
    shuffle(rn)
    return rn

def gen_list_rand_binary_num_str(count: int, min_len: int = 1, max_len: int = 10) -> list | None:
    result: list = []
    if min_len > max_len or min_len < 1:
        return None
    else :
        for _ in range(count):
            num_str = ""
            for _ in range(randint(min_len, max_len)):
                num_str += str(randint(0,1))
            result.append(num_str)

        return result

def check_num_6():
    input_data_num_6 = gen_list_rand_binary_num_str(10)
    for ob in input_data_num_6:
        res = b2int(ob)
        if res is not None:
            print(f"inp - {ob}, res = {res} -- b2int func")
        else:
            pass


def check_num_11():
    list_to_11 = gen_list_rand_int_unic()
    result_11 = raspredelitel(list_to_11)
    if result_11 is not None:
        for ob in result_11:
            print(f"{ob} - raspredelitel func")
    else:
        pass

def check_num_20():
    print(f"{num_20()} - num_20 func")

def check_num_68():
    list_to_68 = gen_list_width_height_rand(5)
    for ob in list_to_68:
        draw_rectangle(*ob)

def check_num_12():
    num_12()


# check_num_6()
# check_num_11()
# check_num_12()
# check_num_20()
# check_num_68()
