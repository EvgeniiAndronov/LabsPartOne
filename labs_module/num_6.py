"""
task:
Без всяких специальных стандартных средств разраб-ть функцию, кот-ая переводит двоич. числа в десятичные.
Алгоритм классич-ий: Число 1101 есть сумма (1 * (2 ** 3) + 1 * (2 ** 2) + 0 * (2 ** 1) + 1 * (2 ** 0)).
Имя функции b2int().

:param value type str:
:return: int or None
"""

def b2int(value: str) -> int | None:

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

if __name__ == '__main__':
    print(f"input 100110\nb2int = {b2int("100110")}\nbinary check {str(bin(b2int("100110")))[2:]}")