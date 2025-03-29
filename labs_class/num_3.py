"""
Найти сумму всех чисел от 0 до 1000, которые делятся на 3 и 5.
"""


class Num_3:

    def __init__(self, delitel1=3, delitel2=5, max_val=1000):
        self.max_val = max_val  # инициализация ключевых параметров
        self.delitel1 = delitel1  # при желании можно будет не указывать значения
        self.delitel2 = delitel2  # в момент инициализации экземпляра класса

    def task(self):  # реализация задачки
        r = [
            i
            for i in range(self.max_val)
            if (i % self.delitel1 == 0) or (i % self.delitel2)
        ]
        return sum(r)


if __name__ == "__main__":
    # вот тут можно не указывать аргументы
    t = Num_3(delitel1=3, delitel2=5, max_val=10)
    print(t.task())
