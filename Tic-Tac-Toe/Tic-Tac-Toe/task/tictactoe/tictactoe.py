# write your code here
Y = 'O'
X = 'X'


class Field:
    H_SEP = '-' * 9

    def __init__(self) -> None:
        self.field = None

    def parse_field(self, cells_string: str):
        cells_string_u = cells_string.replace('_', ' ')
        self.field = [list(cells_string_u[0:3]),
                      list(cells_string_u[3:6]),
                      list(cells_string_u[6:9])]

    def print_field(self):
        print(Field.H_SEP)
        for line in self.field:
            print(f"| {line[0]} {line[1]} {line[2]} |")
        print(Field.H_SEP)

    def is_row_win(self, i: int, c: str) -> bool:
        for j in range(3):
            if self.field[i][j] != c:
                return False
        return True

    def is_col_win(self, j: int, c: str) -> bool:
        for i in range(3):
            if self.field[i][j] != c:
                return False
        return True

    def is_diag_win(self, main: bool, c: str) -> bool:
        if main:
            return self.field[0][0] == self.field[1][1] \
                   == self.field[2][2] == c
        else:
            return self.field[0][2] == self.field[1][1] \
                   == self.field[2][0] == c

    def validate_field(self) -> str:
        empty_count = any(y for x in self.field for y in x if y == ' ')
        x_wins = 0
        o_wins = 0
        for i in range(3):
            if self.is_row_win(i, X):
                x_wins += 1
            if self.is_col_win(i, X):
                x_wins += 1
            if self.is_row_win(i, Y):
                o_wins += 1
            if self.is_col_win(i, Y):
                o_wins += 1
        if self.is_diag_win(True, X):
            x_wins += 1
        if self.is_diag_win(False, X):
            x_wins += 1
        if self.is_diag_win(True, Y):
            o_wins += 1
        if self.is_diag_win(False, Y):
            o_wins += 1

        if x_wins > 1 \
                or o_wins > 1 \
                or x_wins == o_wins == 1:
            return "Impossible"
        elif x_wins == 1:
            return f"{X} wins"
        elif o_wins == 1:
            return f"{Y} wins"
        elif not empty_count:
            return "Draw"
        else:
            return ""

    def next_move(self, c: str):
        while True:
            s = input("Enter the coordinates: ").strip()
            if len(s) != 3 \
                    or not (s[0].isdigit() and s[1] == ' ' and s[2].isdigit()):
                print("You should enter numbers!")
                continue
            if not ('1' <= s[0] <= '3' and '1' <= s[2] <= '3'):
                print("Coordinates should be from 1 to 3!")
                continue
            i = 3 - int(s[2])
            j = int(s[0]) - 1
            if self.field[i][j] != ' ':
                print("This cell is occupied! Choose another one!")
                continue
            else:
                self.field[i][j] = c
                self.print_field()
                break


f = Field()
f.parse_field(' ' * 9)
f.print_field()
is_x = True
while True:
    f.next_move(X if is_x else Y)
    is_x = not is_x
    result = f.validate_field()
    if result:
        print(result)
        break
