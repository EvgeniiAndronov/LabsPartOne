"""
Написать программу по переводу числа из двоичного в десятичное без использования bin()

"""


class Num_6:

    def __init__(self, str_inp_chisl):
        # инициализирую класс с параметром строки, где записано бинарное представление числа
        self.str_inp_chisl = str_inp_chisl

    def __len__(self):  # определяю стандартный метод, где возвращаю длину результирующего числа
        return len(str(self.b2int()))

    def b2int(self):
        # реализация задачи, self нужен для получения переменных из __init__ или получения доступа к другим методам класса
        r = 0
        for i in range(len(self.str_inp_chisl[::-1])):
            r += int(self.str_inp_chisl[::-1][i]) * 2 ** i
        return r

    def test_bin(self):
        test_data = self.b2int()
        result = bin(test_data)
        print(f"{self.str_inp_chisl} - {result[2:]}")


if __name__ == "__main__":
    t = Num_6("10111100")  # инициализирую экземпляр класса

    result = t.b2int()  # считаю задачку, вызывая реализованный в классе метод
    print(f"result = {result}")

    t.test_bin()  # делаю проверку, через уже реализованный метод

    lengh = t.__len__()  # узнаю длинну, через реализованный метод
    print(f"lenght = {lengh}")
