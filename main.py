import logging
logging.basicConfig(filename="Логирование_7_задание.log", level=logging.INFO)
import tkinter as tk
from tkinter import Label

while True:
    try:
        x__1 = int(input('Введите x1 (в диапазоне от 1 до 8) '))
        logging.info('Пользователь ввёл данное значение координаты x1: ' + str(x__1))
        assert 1 <= x__1 <= 8
        break
    except AssertionError:
        print('Введите координату в диапазоне от 1 до 8')
        logging.info('Пользователь ввёл неправильную координату')
    except ValueError:
        print('Введите цифру')
        logging.info("Пользователь ввёл не цифру")

while True:
    try:
        y__1 = int(input('Введите y1 (в диапазоне от 1 до 8) '))
        logging.info('Пользователь ввёл данное значение координаты y1: ' + str(y__1))
        assert 1 <= y__1 <= 8
        break
    except AssertionError:
        print('Введите координату в диапазоне от 1 до 8')
        logging.info('Пользователь ввёл неправильную координату')
    except ValueError:
        print('Введите цифру')
        logging.info('Пользователь ввёл не цифру')

print('Введите координаты второй клетки')

while True:
    try:
        x__2 = int(input('Введите x1 (в диапазоне от 1 до 8)  '))
        logging.info('Пользователь ввёл данное значение координаты x2: ' + str(x__2))
        assert 1 <= x__2 <= 8
        break
    except AssertionError:
        print('Введите координату в диапазоне от 1 до 8')
        logging.info('Пользователь ввёл неправильную координату')
    except ValueError:
        print('Введите цифру')
        logging.info('Пользователь ввёл не цифру')

while True:
    try:
        y__2 = int(input('Введите y2 (в диапазоне от 1 до 8)  '))
        logging.info('Пользователь ввёл данное значение координаты y2: ' + str(y__2))
        assert 1 <= y__2 <= 8
        assert y__1 != y__2 or x__1 != x__2
        break
    except AssertionError:
        print('Координата не в диапозоне от 1 до 8 или вы ввели одинаковые клетки')
        logging.info('Пользователь ввёл неправильную координату')
    except ValueError:
        print('Введите цифру')
        logging.info('Пользователь ввёл не цифру')

def color_check(x__1, y__1, x__2, y__2):
    if (x__1 + y__1) % 2 == (x__2 + y__2) % 2:
        return True
    else:
        return False


def knight_check(x__1, y__1, x__2, y__2):
    if (x__2 - x__1) ** 2 + (y__2 - y__1) ** 2 == 5:
        return True
    else:
        return False


def rook_check(x__1, y__1, x__2, y__2):
    if x__1 == x__2 or y__1 == y__2:
        return True
    else:
        return False


def bishop_check(x__1, y__1, x__2, y__2):
    if (x__2 - x__1) ** 2 == (y__2 - y__1) ** 2:
        return True
    else:
        return False


def queen_check(x__1, y__1, x__2, y__2):
    if rook_check(x__1, y__1, x__2, y__2) or bishop_check(x__1, y__1, x__2, y__2):
        return True
    else:
        return False


if color_check(x__1, y__1, x__2, y__2):
    print('Клетки одного цвета')
    logging.info("Пользователь ввёл клетки одного цвета")
else:
    print('Клетки разного цвета')
    logging.info("Пользователь ввёл клетки разного цвета")

# Рисуем доску
figure = ''


def draw_desk(x__1, y__1, x__2, y__2):
    print('Откройте окно')
    BRD_ROWS = BRD_COLS = 8
    CELL_SZ = 50

    root = tk.Tk()
    root.title('Закройте окно для продолжения')
    Label(text="Начальная клетка - зелёный, Конечная клетка - синий, Промежуточное значение - красный ", width=100,
          height=5) \
        .pack()
    canvas = tk.Canvas(root, width=CELL_SZ * BRD_ROWS, height=CELL_SZ * BRD_COLS)

    cell_colors = ['white', 'black']
    ci = 0  # цветовой индекс

    # Рисует пустую доску
    def draw_empty_desk():
        if row == 8 - y__1 and col == x__1 - 1:
            canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='green')
        elif row == 8 - y__2 and col == x__2 - 1:
            canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='blue')
        else:
            canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill=cell_colors[ci])

    for row in range(BRD_ROWS):
        for col in range(BRD_COLS):
            x_0, y_0 = col * CELL_SZ, row * CELL_SZ
            x_1, y_1 = col * CELL_SZ + CELL_SZ, row * CELL_SZ + CELL_SZ

            if figure == 'ферзь' or figure == 'Ферзь' or figure == 'ладья' or figure == 'Ладья':
                if row == 8 - y__1 and col == x__2 - 1:
                    canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='red')
                else:
                    draw_empty_desk()
            elif figure == 'слон' or figure == 'Слон':
                if bishop_check(x__1, y__1, 8-row, col+1) and bishop_check(x__2, y__2, 8-row, col+1):
                    canvas.create_rectangle((x_0, y_0), (x_1, y_1), fill='red')
                else:
                    draw_empty_desk()
            else:
                draw_empty_desk()

            ci = not ci

        ci = not ci

    canvas.pack()

    root.mainloop()


draw_desk(x__1, y__1, x__2, y__2)

while True:
    a = 1
    figure = input('Введите название фигуры: Ферзь/Ладья/Слон/Конь ')
    logging.info("Пользователь выбрал данную фигуру: " + str(figure))
    if figure == 'ферзь' or figure == 'Ферзь':
        if queen_check(x__1, y__1, x__2, y__2):
            print('Ход возможен')
            logging.info("Ход пользователя возможен " )
        else:
            print('Ход невозможен')
            print('Реализация за два хода')
            logging.info("Ход пользователя невозможен, но реализуем за два хода ")
            draw_desk(x__1, y__1, x__2, y__2)
    elif figure == 'ладья' or figure == ('Ладья'):
        if rook_check(x__1, y__1, x__2, y__2):
            print('Ход возможен')
            logging.info("Ход пользователя возможен ")
        else:
            print('Ход невозможен')
            print('Реализация за два хода')
            logging.info("Ход пользователя невозможен, но реализуем за два хода ")
            draw_desk(x__1, y__1, x__2, y__2)
    elif figure == 'слон' or figure == ('Слон'):
        if bishop_check(x__1, y__1, x__2, y__2):
            print('Ход возможен')
            logging.info("Ход пользователя возможен ")
        elif color_check(x__1, y__1, x__2, y__2):
            print('Ход невозможен')
            print('Реализация за два хода')
            logging.info("Ход пользователя невозможен, но реализуем за два хода ")
            draw_desk(x__1, y__1, x__2, y__2)

    elif figure == 'конь' or figure == ('Конь'):
        if knight_check(x__1, y__1, x__2, y__2):
            print('Ход возможен')
            logging.info("Ход пользователя возможен ")
        else:
            print('Ход невозможен')
            logging.info("Ход пользователя невозможен ")
    else:
        a = 0
        print('Неверная фигура')
        logging.info("Пользователь неправильно выбрал фигуру ")
    if a:
        break