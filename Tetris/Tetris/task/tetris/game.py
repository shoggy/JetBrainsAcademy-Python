# Write your code here
from io import StringIO

figure_size = 4
segs = {
    'O': [[1, 5, 6, 2]],
    'I': [[1, 5, 9, 13], [0, 1, 2, 3]],
    'S': [[2, 1, 5, 4], [1, 5, 6, 10]],
    'Z': [[1, 2, 6, 7], [2, 6, 5, 9]],
    'L': [[1, 5, 9, 10], [2, 6, 5, 4], [1, 2, 6, 10], [3, 2, 1, 5]],
    'J': [[2, 6, 10, 9], [6, 2, 1, 0], [2, 1, 5, 9], [1, 5, 6, 7]],
    'T': [[1, 5, 9, 6], [1, 4, 5, 6], [2, 6, 10, 5], [1, 2, 3, 6]]
}


class Figure:

    def __init__(self, letter, row, col) -> None:
        super().__init__()
        self.row = row
        self.col = col
        self.points_list = segs[letter]
        self.rotation = 0

    def points(self) -> list:
        return self.points_list[self.rotation]

    def rotate(self) -> None:
        self.rotation = (self.rotation + 1) % len(self.points_list)


class TetrisException(Exception):
    pass


class Tetris:

    @staticmethod
    def iterate_figure_points(figure: Figure) -> tuple:
        for d_row in range(figure_size):
            for d_col in range(figure_size):
                if d_row * figure_size + d_col in figure.points():
                    row = figure.row + d_row
                    col = figure.col + d_col
                    yield row, col

    def __init__(self, height=20, width=10) -> None:
        super().__init__()
        self.height = height
        self.width = width
        self.field = [[0] * width for _ in range(height)]
        self.figure: Figure = None

    def __str__(self) -> str:
        output = StringIO()
        figure_points = set(Tetris.iterate_figure_points(self.figure)) if self.figure else set()
        for row_idx, row in enumerate(self.field):
            print(' '.join('0' if elem or (row_idx, col_idx) in figure_points else '-'
                           for col_idx, elem in enumerate(row)),
                  file=output)
        result = output.getvalue()
        output.close()
        return result

    def new_figure(self, letter) -> None:
        self.figure = Figure(letter, 0, (self.width - figure_size) // 2)
        if self.intersects():
            raise TetrisException()
        print(self)

    def intersects(self) -> bool:
        if self.figure is None:
            return False
        for row, col in Tetris.iterate_figure_points(self.figure):
            if not (0 <= row < self.height) or \
                    not (0 <= col < self.width) or \
                    self.field[row][col]:
                return True
        return False

    def intersects_next_down(self) -> bool:
        for row, col in Tetris.iterate_figure_points(self.figure):
            if row + 1 >= self.height or self.field[row + 1][col]:
                return True
        return False

    def freeze(self) -> None:
        if self.figure is None:
            return
        for row, col in Tetris.iterate_figure_points(self.figure):
            self.field[row][col] = 1
        self.figure = None

    def remove_full_lines(self) -> None:
        i = self.height - 1
        while i >= 0:
            if all(self.field[i]):
                del self.field[i]
                self.field.insert(0, [0] * self.width)
            else:
                i -= 1
        print(self)

    def move_horizontal(self, d_col):
        old_col = self.figure.col
        self.figure.col += d_col
        if self.intersects():
            self.figure.col = old_col

    def move_left(self):
        self.move_horizontal(-1)

    def move_right(self):
        self.move_horizontal(1)

    def move_down(self):
        if self.intersects_next_down():
            if self.figure.row == 0:
                print(self)
                raise TetrisException('full height')
            else:
                self.freeze()
        else:
            self.figure.row += 1
            if self.intersects():
                self.figure.row -= 1

    def rotate(self):
        old_rotation = self.figure.rotation
        self.figure.rotate()
        if self.intersects():
            self.figure.rotation = old_rotation

    def make_move(self, cmd):
        if self.figure is not None:
            if cmd == 'left':
                self.move_left()
                self.move_down()
            elif cmd == 'right':
                self.move_right()
                self.move_down()
            elif cmd == 'down':
                self.move_down()
            elif cmd == 'rotate':
                self.rotate()
                self.move_down()
        print(self)


[cols, rows] = [int(x) for x in input().split()]
game = Tetris(rows, cols)
print(game)
while True:
    cmd = input()
    try:
        if cmd == 'piece':
            game.new_figure(input())
        elif cmd in ('left', 'right', 'down', 'rotate'):
            game.make_move(cmd)
        elif cmd == 'break':
            game.remove_full_lines()
        elif cmd == 'exit':
            break
    except TetrisException:
        print('Game Over!')
        break
