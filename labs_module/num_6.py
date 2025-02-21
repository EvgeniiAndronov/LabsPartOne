def b2int(value: str) -> int | None:
    """
    task:
    Без всяких специальных стандартных средств разраб-ть функцию, кот-ая переводит двоич. числа в десятичные.
    Алгоритм классич-ий: Число 1101 есть сумма (1 * (2 ** 3) + 1 * (2 ** 2) + 0 * (2 ** 1) + 1 * (2 ** 0)).
    Имя функции b2int().
    
    :param value type str:
    :return: int or None
    """

    try:
        result_data: int = 0
        st: int = 0
        binary_num: str = value[::-1]

        for ob in binary_num:
            result_data += int(ob) * 2 ** st
            st += 1

        return result_data
    except ValueError:
        print("Error in input value!")
        return None
    except TypeError:
        print("Error in input value!(type err)")
        return None
    except Exception as e:
        print(f"Some error occured: {e}")
        return None


# def helper(n: int) -> (int, int):
#     return (n % 2), (n // 2)

# def int2b(value: int) -> str | None:
#     if value == 0:
#         return "0"
#     elif value == 1:
#         return "1"
#     else:
#         str_result: str = ""
#         flag: bool = True
#
#         try:
#             while flag:
#                 ost, cel = helper(value)
#                 value = cel
#
#                 str_result += str(ost)
#                 if value == 1 or value == 0:
#                     flag = False
#                     str_result += str(value)
#
#             return str_result[::-1]
#         except ValueError:
#             print("Error in input value!")
#             return None
#         except TypeError:
#             print("Error in input value!(type err)")
#             return None
#         except Exception as e:
#             print(f"Some error occured: {e}")
#             return None