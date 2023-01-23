from random import randint


class Ship:
    def __init__(self, length, tp=1, x=None, y=None):
        self._length = length
        self._x = x
        self._y = y
        self._tp = tp
        self._is_move = True
        self._cells = [1 for _ in range(length)]
        self._coords = [] if x is None and y is None else [[x, y], ]

    def set_start_coords(self, x, y):
        self._x = x
        self._y = y

    def get_start_coords(self):
        return self._x, self._y

    def move(self, go):
        if self._is_move is True and self._tp == 1:
            for i in range(len(self._coords)):
                self._coords[i][1] += go
        elif self._is_move is True and self._tp == 2:
            for i in range(len(self._coords)):
                self._coords[i][0] += go

    def is_collide(self, ship):
        for i in self._coords:
            if i in ship._coords:
                return True
        for i in range(min((len(self._coords), len(ship._coords)))):
            if (self._coords[i][0] == ship._coords[i][0] and abs(self._coords[i][1] - ship._coords[i][1]) == 1) or (
                    abs(self._coords[i][0] - ship._coords[i][0]) == 1 and self._coords[i][1] == ship._coords[i][1]) or (
                    abs(self._coords[i][0] - ship._coords[i][0]) == 1 and abs(
                    self._coords[i][1] - ship._coords[i][1]) == 1):
                return True
        return False

    def is_out_pole(self, size):
        if self._tp == 1:
            if self._x + self._length > size:
                return True
        if self._tp == 2:
            if self._y + self._length > size:
                return True
        return False

    def __getitem__(self, item):
        return self._cells[item]

    def __setitem__(self, key, value):
        self._cells[key] = value


class GamePole:
    SIZE_CLASS = None

    def __new__(cls, *args, **kwargs):
        cls.SIZE_CLASS = args[0]
        return super().__new__(cls)

    def __init__(self, size):
        self._size = size
        self._pole = [[0 for _ in range(self._size)] for _ in range(self._size)]
        self._flag = False
        self._ships_hor = []
        self._ships_ver = []
        self._ships = [Ship(3, tp=2), Ship(3, tp=2)]

    def __setattr__(self, key, value):
        if key == '_size' and value <= 0:
            raise ValueError
        super().__setattr__(key, value)

    def place_vertical_ship(self, ship):
        while True:

            self._flag = False

            for m in range(len(self._pole) + 1 - ship._length):

                for p in range(len(self._pole[m])):
                    check = 0
                    for k in range(ship._length):

                        i, j = m + k, p
                        if 0 < i < len(self._pole) - 1 and 0 < j < len(self._pole) - 1:
                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i][j - 1], self._pole[i - 1][j - 1],
                                     self._pole[i - 1][j], self._pole[i - 1][j + 1],
                                     self._pole[i + 1][j - 1], self._pole[i + 1][j],
                                     self._pole[i + 1][j + 1])) == 0:
                                check += 1
                        elif i == 0 and j == 0:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i + 1][j],
                                     self._pole[i + 1][j + 1])) == 0:
                                check += 1

                        elif (0 < i < len(self._pole) - 1) and j == 0:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i - 1][j], self._pole[i - 1][j + 1],
                                     self._pole[i + 1][j],
                                     self._pole[i + 1][j + 1])) == 0:
                                check += 1
                        elif i == len(self._pole) - 1 and j == 0:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i - 1][j], self._pole[i - 1][j + 1],
                                     self._pole[i][j + 1])) == 0:
                                check += 1
                        elif i == len(self._pole) - 1 and 0 < j < len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j - 1], self._pole[i][j + 1], self._pole[i - 1][j - 1],
                                     self._pole[i - 1][j], self._pole[i - 1][j + 1])) == 0:
                                check += 1
                        elif i == len(self._pole) - 1 and j == len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j - 1], self._pole[i - 1][j - 1],
                                     self._pole[i - 1][j])) == 0:
                                check += 1
                        elif (0 < i < len(self._pole) - 1) and j == len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i + 1][j], self._pole[i + 1][j - 1], self._pole[i][j - 1],
                                     self._pole[i - 1][j - 1], self._pole[i - 1][j])) == 0:
                                check += 1
                        elif i == 0 and j == len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i + 1][j], self._pole[i + 1][j - 1],
                                     self._pole[i][j - 1])) == 0:
                                check += 1
                        elif i == 0 and (0 < j < len(self._pole) - 1):

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i + 1][j + 1], self._pole[i + 1][j],
                                     self._pole[i + 1][j - 1], self._pole[i][j - 1])) == 0:
                                check += 1
                    if check == ship._length:
                        self._flag = True
                        break
                    else:
                        continue
                if self._flag is True:
                    break
            if self._flag is True:
                for k in range(ship._length):
                    i, j = m + k, p
                    self._pole[i][j] = 1
                    ship._coords.append([i, j])
                break
            else:
                continue

    def place_horizontal_ship(self, ship):
        while True:
            self._flag = False
            for m in range(len(self._pole)):

                for p in range(len(self._pole[m]) + 1 - ship._length):
                    check = 0
                    for k in range(ship._length):

                        i, j = m, p + k
                        if 0 < i < len(self._pole) - 1 and 0 < j < len(self._pole) - 1:
                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i][j - 1], self._pole[i - 1][j - 1],
                                     self._pole[i - 1][j], self._pole[i - 1][j + 1],
                                     self._pole[i + 1][j - 1], self._pole[i + 1][j],
                                     self._pole[i + 1][j + 1])) == 0:
                                check += 1
                        elif i == 0 and j == 0:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i + 1][j],
                                     self._pole[i + 1][j + 1])) == 0:
                                check += 1

                        elif (0 < i < len(self._pole) - 1) and j == 0:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i - 1][j], self._pole[i - 1][j + 1],
                                     self._pole[i + 1][j],
                                     self._pole[i + 1][j + 1])) == 0:
                                check += 1
                        elif i == len(self._pole) - 1 and j == 0:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i - 1][j], self._pole[i - 1][j + 1],
                                     self._pole[i][j + 1])) == 0:
                                check += 1
                        elif i == len(self._pole) - 1 and 0 < j < len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j - 1], self._pole[i][j + 1], self._pole[i - 1][j - 1],
                                     self._pole[i - 1][j], self._pole[i - 1][j + 1])) == 0:
                                check += 1
                        elif i == len(self._pole) - 1 and j == len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j - 1], self._pole[i - 1][j - 1],
                                     self._pole[i - 1][j])) == 0:
                                check += 1
                        elif (0 < i < len(self._pole) - 1) and j == len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i + 1][j], self._pole[i + 1][j - 1], self._pole[i][j - 1],
                                     self._pole[i - 1][j - 1], self._pole[i - 1][j])) == 0:
                                check += 1
                        elif i == 0 and j == len(self._pole) - 1:

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i + 1][j], self._pole[i + 1][j - 1],
                                     self._pole[i][j - 1])) == 0:
                                check += 1
                        elif i == 0 and (0 < j < len(self._pole) - 1):

                            if self._pole[i][j] == 0 and sum(
                                    (self._pole[i][j + 1], self._pole[i + 1][j + 1], self._pole[i + 1][j],
                                     self._pole[i + 1][j - 1], self._pole[i][j - 1])) == 0:
                                check += 1
                    if check == ship._length:
                        self._flag = True
                        break
                    else:
                        continue
                if self._flag is True:
                    break
            if self._flag is True:
                for k in range(ship._length):
                    i, j = m, p + k
                    self._pole[i][j] = 1
                    ship._coords.append([i, j])
                break
            else:
                continue

    def init(self):
        self._ships_hor = list(filter(lambda x: x._tp == 1, self._ships))
        self._ships_ver = list(filter(lambda x: x._tp == 2, self._ships))
        for i in self._ships_hor:
            self.place_horizontal_ship(i)
            i._x = i._coords[0][1]
            i._y = i._coords[0][0]
        for i in self._ships_ver:
            self.place_vertical_ship(i)
            i._x = i._coords[0][1]
            i._y = i._coords[0][0]

    def get_ships(self):
        return self._ships

    def blow_neighbor_cells(self, i, j):
        if 0 < i < len(self._pole) - 1 and 0 < j < len(self._pole) - 1:
            self._pole[i][j + 1] = 2
            self._pole[i][j - 1] = 2
            self._pole[i - 1][j - 1] = 2
            self._pole[i - 1][j] = 2
            self._pole[i - 1][j + 1] = 2
            self._pole[i + 1][j - 1] = 2
            self._pole[i + 1][j] = 2
            self._pole[i + 1][j + 1] = 2


        elif i == 0 and j == 0:
            self._pole[i][j + 1] = 2
            self._pole[i + 1][j] = 2
            self._pole[i + 1][j + 1] = 2


        elif (0 < i < len(self._pole) - 1) and j == 0:
            self._pole[i][j + 1] = 2
            self._pole[i - 1][j] = 2
            self._pole[i - 1][j + 1] = 2
            self._pole[i + 1][j] = 2
            self._pole[i + 1][j + 1] = 2


        elif i == len(self._pole) - 1 and j == 0:
            self._pole[i - 1][j] = 2
            self._pole[i - 1][j + 1] = 2
            self._pole[i][j + 1] = 2

        elif i == len(self._pole) - 1 and 0 < j < len(self._pole) - 1:
            self._pole[i][j - 1] = 2
            self._pole[i][j + 1] = 2
            self._pole[i - 1][j - 1] = 2
            self._pole[i - 1][j] = 2
            self._pole[i - 1][j + 1] = 2


        elif i == len(self._pole) - 1 and j == len(self._pole) - 1:
            self._pole[i][j - 1] = 2
            self._pole[i - 1][j - 1] = 2
            self._pole[i - 1][j] = 2


        elif (0 < i < len(self._pole) - 1) and j == len(self._pole) - 1:
            self._pole[i + 1][j] = 2
            self._pole[i + 1][j - 1] = 2
            self._pole[i][j - 1] = 2
            self._pole[i - 1][j - 1] = 2
            self._pole[i - 1][j] = 2


        elif i == 0 and j == len(self._pole) - 1:
            self._pole[i + 1][j] = 2
            self._pole[i + 1][j - 1] = 2
            self._pole[i][j - 1] = 2

        elif i == 0 and (0 < j < len(self._pole) - 1):
            self._pole[i][j + 1] = 2
            self._pole[i + 1][j + 1] = 2
            self._pole[i + 1][j] = 2
            self._pole[i + 1][j - 1] = 2
            self._pole[i][j - 1] = 2

    def check_coords(self, i, j):
        if 0 < i < len(self._pole) - 1 and 0 < j < len(self._pole) - 1:
            if self._pole[i][j] == 0 and sum(
                    (self._pole[i][j + 1], self._pole[i][j - 1], self._pole[i - 1][j - 1],
                     self._pole[i - 1][j], self._pole[i - 1][j + 1],
                     self._pole[i + 1][j - 1], self._pole[i + 1][j],
                     self._pole[i + 1][j + 1])) == 0:
                return True
        elif i == 0 and j == 0:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i][j + 1], self._pole[i + 1][j],
                     self._pole[i + 1][j + 1])) == 0:
                return True

        elif (0 < i < len(self._pole) - 1) and j == 0:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i][j + 1], self._pole[i - 1][j], self._pole[i - 1][j + 1],
                     self._pole[i + 1][j],
                     self._pole[i + 1][j + 1])) == 0:
                return True
        elif i == len(self._pole) - 1 and j == 0:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i - 1][j], self._pole[i - 1][j + 1],
                     self._pole[i][j + 1])) == 0:
                return True
        elif i == len(self._pole) - 1 and 0 < j < len(self._pole) - 1:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i][j - 1], self._pole[i][j + 1], self._pole[i - 1][j - 1],
                     self._pole[i - 1][j], self._pole[i - 1][j + 1])) == 0:
                return True
        elif i == len(self._pole) - 1 and j == len(self._pole) - 1:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i][j - 1], self._pole[i - 1][j - 1],
                     self._pole[i - 1][j])) == 0:
                return True
        elif (0 < i < len(self._pole) - 1) and j == len(self._pole) - 1:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i + 1][j], self._pole[i + 1][j - 1], self._pole[i][j - 1],
                     self._pole[i - 1][j - 1], self._pole[i - 1][j])) == 0:
                return True
        elif i == 0 and j == len(self._pole) - 1:

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i + 1][j], self._pole[i + 1][j - 1],
                     self._pole[i][j - 1])) == 0:
                return True
        elif i == 0 and (0 < j < len(self._pole) - 1):

            if self._pole[i][j] == 0 and sum(
                    (self._pole[i][j + 1], self._pole[i + 1][j + 1], self._pole[i + 1][j],
                     self._pole[i + 1][j - 1], self._pole[i][j - 1])) == 0:
                return True
        return False

    def move_ships(self):
        if len(self._ships_ver) > 0:
            for l in range(len(self._ships_ver)):
                tail_ordinata, tail_abscissa = self._ships_ver[l]._coords[-1][0], self._ships_ver[l]._coords[-1][1]
                if not self._ships_ver[l]._coords[0][0] - 1 < 0:
                    i = self._ships_ver[l]._coords[0][0] - 1
                    i_starting = self._ships_ver[l]._coords[0][0]
                    j = self._ships_ver[l]._coords[0][1]
                    self._pole[i_starting][j] = 0
                    if self.check_coords(i, j):
                        for g in range(len(self._ships_ver[l]._coords)):
                            self._pole[self._ships_ver[l]._coords[g][0] - 1][self._ships_ver[l]._coords[g][1]] = 1
                            self._ships_ver[l]._coords[g][0] -= 1
                        self._pole[tail_ordinata][tail_abscissa] = 0
                    break

                start_ordinata, start_abscissa, = self._ships_ver[l]._coords[0][0], self._ships_ver[l]._coords[0][1]
                if not self._ships_ver[l]._coords[-1][0] + 1 > len(self._pole) - 1:
                    i = self._ships_ver[l]._coords[-1][0] + 1
                    i_starting = self._ships_ver[l]._coords[-1][0]
                    j = self._ships_ver[l]._coords[-1][1]
                    self._pole[i_starting][j] = 0
                    if self.check_coords(i, j):
                        for g in range(len(self._ships_ver[l]._coords)):
                            self._pole[self._ships_ver[l]._coords[g][0] + 1][self._ships_ver[l]._coords[g][1]] = 1
                            self._ships_ver[l]._coords[g][0] += 1
                        self._pole[start_ordinata][start_abscissa] = 0
                        break

        if len(self._ships_hor) > 0:
            for c in range(len(self._ships_hor)):
                tail_ordinata, tail_abscissa = self._ships_hor[c]._coords[-1][0], self._ships_hor[c]._coords[-1][1]
                if not self._ships_hor[c]._coords[0][1] - 1 < 0:
                    i = self._ships_hor[c]._coords[0][0]
                    j = self._ships_hor[c]._coords[0][1] - 1
                    j_starting = self._ships_hor[c]._coords[0][1]
                    self._pole[i][j_starting] = 0
                    if self.check_coords(i, j):
                        for y in range(len(self._ships_hor[c]._coords)):
                            self._pole[self._ships_hor[c]._coords[y][0]][self._ships_hor[c]._coords[y][1] - 1] = 1
                            self._ships_hor[c]._coords[y][1] -= 1
                        self._pole[tail_ordinata][tail_abscissa] = 0
                        break

                start_ordinata, start_abscissa = self._ships_hor[c]._coords[0][0], self._ships_hor[c]._coords[0][1]
                if not self._ships_hor[c]._coords[-1][1] + 1 > len(self._pole) - 1:
                    i = self._ships_hor[c]._coords[-1][0]
                    j = self._ships_hor[c]._coords[-1][1] + 1
                    j_starting = self._ships_hor[c]._coords[-1][1]
                    self._pole[i][j_starting] = 0
                    if self.check_coords(i, j):
                        for y in range(len(self._ships_hor[c]._coords)):
                            self._pole[self._ships_hor[c]._coords[y][0]][self._ships_hor[c]._coords[y][1] + 1] = 1
                            self._ships_hor[c]._coords[y][1] += 1
                        self._pole[start_ordinata][start_abscissa] = 0
                        break

    def show(self):
        for i in self._pole:
            print(*i)

    def get_pole(self):
        return tuple(tuple(i) for i in self._pole)


class SeaBattle:
    a = GamePole(3)
    a.init()
    b = GamePole(3)
    b.init()

    def check_coords(self, x, y):
        return 0 <= x <= GamePole.SIZE_CLASS - 1 or 0 <= y <= GamePole.SIZE_CLASS - 1

    def human_go(self):
        """Ход игрока (вводятся координаты в одному строчку через пробел, отсчет с 0)"""
        while True:
            print('------------')
            print('Корабли компьютера')
            for v in self.b._pole:
                for e in v:
                    if e == 0 or e == 1:
                        printable = '#'
                    elif e == 2:
                        printable = 2
                    else:
                        printable = 4
                    print(printable, end='')
                print('', end='\n')
            # print('------------') # закомментить либо убрать
            # print('Открытое расположение кораблей компьютера (для теста)') # закомментить либо убрать
            # self.b.show()

            print('Пожалуйста введите координаты ячейки, по которой будет произведен выстрел')
            x, y = map(int, input().split())

            if not self.check_coords(x, y):
                print(f'Неверные координаты. Диапазон координат от 0 до {GamePole.SIZE_CLASS - 1}')
                continue
            if self.b._pole[x][y] == 3 or self.b._pole[x][y] == 4:
                print(f'В ячейку [{x}, {y}] выстрел уже производился. Попробуйте еще раз.')
                continue
            if self.b._pole[x][y] == 2:
                print(f'В ячейке [{x}, {y}] не может быть кораблей. Попробуйте еще раз.')
                continue
            for i in self.b._ships:
                good_shot_flag = False
                if [x, y] in i._coords:
                    i._cells[i._coords.index([x, y])] = 4
                    if not all(map(lambda x: x == 4, i._cells)):
                        print('Подбил! Ход за вами')
                        self.b._pole[x][y] = 4
                        good_shot_flag = True
                        break
                    if all(map(lambda x: x == 4, i._cells)):
                        for j in i._coords:
                            self.b.blow_neighbor_cells(j[0], j[1])
                        for coords_pair in i._coords:
                            self.b._pole[coords_pair[0]][coords_pair[1]] = 2
                        print('Убил! Ход за вами')
                        good_shot_flag = True
                        break
            if all(map(lambda x: 1 not in x, self.b._pole)):
                print('Вы победили!')
                print('------------')
                self.b.show()
                break
            if good_shot_flag is True:
                continue
            else:
                print('Мимо')
                self.b._pole[x][y] = 3
                self.b.show()
                print('------------')
                break

    def computer_go(self):
        """Ход компьютера"""
        while True:

            print('Корабли игрока')
            self.a.show()
            print('Компьютер производит выстрел')
            x, y = randint(0, GamePole.SIZE_CLASS - 1), randint(0, GamePole.SIZE_CLASS - 1)
            if self.a._pole[x][y] == 3 or self.a._pole[x][y] == 4:
                continue
            if self.a._pole[x][y] == 2:
                continue
            for i in self.a._ships:
                good_shot_flag = False
                if [x, y] in i._coords:
                    i._cells[i._coords.index([x, y])] = 4
                    if not all(map(lambda x: x == 4, i._cells)):
                        print('Подбил! Ход за компьютером')
                        self.a._pole[x][y] = 4
                        good_shot_flag = True
                        break
                    if all(map(lambda x: x == 4, i._cells)):
                        for j in i._coords:
                            self.a.blow_neighbor_cells(j[0], j[1])
                        for coords_pair in i._coords:
                            self.a._pole[coords_pair[0]][coords_pair[1]] = 2
                        print('Убил! Ход за компьютером')
                        good_shot_flag = True
                        break
            if all(map(lambda x: 1 not in x, self.a._pole)):
                print('Копмьютер победил!')
                print('------------')
                self.a.show()
                break
            if good_shot_flag is True:
                continue
            else:
                self.a._pole[x][y] = 3
                print('''Мимо''')
                self.a.show()
                print('------------')
                break

    def Let_The_Battle_Begin(self):
        while True:
            if all(map(lambda x: 1 not in x, self.a._pole)) or all(map(lambda x: 1 not in x, self.b._pole)):
                break
            self.computer_go()
            self.human_go()
