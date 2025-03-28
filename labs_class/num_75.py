"""
Из русских букв составить произвольную последовательность 25
элементов и убрать все повторяющиеся элементы заменив их символом "0"
"""

from ramdom import choice


class Num_75:  # родительский класс

    def __init__(self, len_line=25):  # инициализация со значением - длинны строки
        self.len_line = len_line

    def create_rand_line(self):  # реализация метода генерации строки
        line_s = [chr(a) for a in range(ord("а"), ord("я") + 1)]
        line_s.append("ё")
        line = []
        for _ in range(self.len_line):
            line.append(choice(line_s))
        return line


class New_num_75(Num_75):  # наследуемся от родительского класса

    def task(self):  # реализуем метод для решения задачки
        line = self.create_rand_line()  # вызываем метод генерации строки из родительского метода
        pr = []
        for i in range(len(line) - 1):
            if not line[i] in pr:
                pr.append(line[i])
            if line[i + 1] in pr:
                pr.append("0")
            else:
                pr.append(line[i + 1])

        return pr, line


if __name__ == "__main__":
    t = New_num_75(len_line=10)  # инициализирую экземпляр класса(дочернего)
    result, line = t.task()  # получаю исходный список и измененный
    print(f"result = \t{result}\nline = \t{line}")
