from random import randint

def gen_list_rand_int(count: int, min: int = 0, max: int = 100) -> list:
    result: list = []
    for _ in range(count):
        result.append(randint(min, max))

    return result

