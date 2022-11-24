def welcome():
    print("""Добро пожаловать в
 крестики-нолики!
 Формат ввода: x,y
   x - номер строки
   y - номер столбца""")


def pole():
    print(f"  0 1 2")
    print(f"0 {cells[0][0]} {cells[0][1]} {cells[0][2]}")
    print(f"1 {cells[1][0]} {cells[1][1]} {cells[1][2]}")
    print(f"2 {cells[2][0]} {cells[2][1]} {cells[2][2]}")


def ask():
    while True:
        coor = input("      Ваш ход: ").split()

        if len(coor) != 2:
            print("Введите 2 координаты")
            continue

        x, y = coor

        if not(x.isdigit()) or not(y.isdigit()):
            print("Введите числа")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2:
            print("Координаты не из диапозона")
            continue

        if cells[x][y] != " ":
            print("Клетка занята")
            continue
        return x, y


def win():
    victory = (((0, 0), (1, 0), (2, 0)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)),
               ((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0)))
    for coor in victory:
        symbols = []
        for a in coor:
            symbols.append(cells[a[0]][a[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X! :)")
            return True
        if symbols == ["O", "O", "O"]:
            print("Выиграл O! :)")
            return True
    return False


welcome()
cells = [[" ",  " ",  " "], [" ",  " ",  " "], [" ",  " ",  " "]]
count = 0
while True:
    count += 1
    pole()
    if count % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")

    c, b = ask()

    if count % 2 == 1:
        cells[c][b] = "X"
    else:
        cells[c][b] = "O"

    if win():
        break
    if count == 9:
        print("Ничья")
        break
