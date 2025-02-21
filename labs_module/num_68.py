"""
Проверив и поняв как? функция (ниже) принтует
квадрат в полуграфике: создать функцию, кот. рисует
прямоугольники размером 2x2, 2x3, 3x3. Для этого
вам понадобятся символы полуграфики с кодами 0x252C и 0x2534
"""

def draw_rectangle(width: int, height: int) -> None:
    top_left = '╔'
    top_right = '╗'
    bottom_left = '╚'
    bottom_right = '╝'
    horizontal = '═'
    vertical = '║'

    midle_count_step = width - 2

    print(f"{top_left}{midle_count_step * horizontal}{top_right}\t\twidth = {width}; height = {height}")

    for _ in range(height - 2):
        print(f"{vertical}{' ' * midle_count_step}{vertical}")

    print(f"{bottom_left}{horizontal * midle_count_step}{bottom_right}")

if __name__ == '__main__':
    draw_rectangle(2, 2)
    print()
    draw_rectangle(3, 3)
    print()
    draw_rectangle(2, 3)