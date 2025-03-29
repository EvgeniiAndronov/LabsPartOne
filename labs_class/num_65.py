"""
Из строки «Privet ot Vasi Pupkina» сделать 4-х элем-ный список
и, потом, как-то срезав у него «rivet t asi upkina», слить остатки и
в конце вывести уже оставшуюся опять строку, но не «PoVP», а
«pOvp»
"""


class StringProcessor:
    def __init__(self, input_string):
        self.input_string = input_string
        self.parts = []
        self.sliced = []
        self.combined = ""
        self.transformed = ""

    def split_into_four(self):
        """Разбиваем строку на 4 элемента по пробелам"""
        self.parts = self.input_string.split()
        if len(self.parts) != 4:
            raise ValueError("Строка должна содержать ровно 4 элемента после разбиения")

    def slice_elements(self):
        """Срезаем первые символы из каждого элемента"""
        self.sliced = [word[0] for word in self.parts]

    def combine_remaining(self):
        """Объединяем оставшиеся символы"""
        self.combined = "".join(self.sliced)

    def transform_case(self):
        """Инвертируем регистр символов"""
        self.transformed = self.combined.swapcase()


class Task(StringProcessor):
    def process(self):
        """Запуск всего процесса"""
        self.split_into_four()
        self.slice_elements()
        self.combine_remaining()
        self.transform_case()
        return self.transformed


# Использование
if __name__ == "__main__":
    processor = Task("Privet ot Vasi Pupkina")
    result = processor.process()
    print(result)  # -> pOvp
