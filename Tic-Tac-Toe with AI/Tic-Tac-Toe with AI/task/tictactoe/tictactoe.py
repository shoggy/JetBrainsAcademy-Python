# write your code here
from math import inf

Y = 'O'
X = 'X'
USER = 'user'
EASY = 'easy'
MEDIUM = 'medium'
HARD = 'hard'


def other_char(c):
    return X if c == Y else Y


class Minimax():
    def wins(self, state, player: str) -> bool:
        return state[0][0] == state[0][1] == state[0][2] == player \
               or state[1][0] == state[1][1] == state[1][2] == player \
               or state[2][0] == state[2][1] == state[2][2] == player \
               or state[0][0] == state[1][0] == state[2][0] == player \
               or state[0][1] == state[1][1] == state[2][1] == player \
               or state[0][2] == state[1][2] == state[2][2] == player \
               or state[0][0] == state[1][1] == state[2][2] == player \
               or state[2][0] == state[1][1] == state[0][2] == player

    def evaluate(self, state, ai: str) -> int:
        if self.wins(state, ai):
            return +1
        if self.wins(state, other_char(ai)):
            return -1
        return 0

    def game_over(self, state) -> bool:
        return self.wins(state, X) or self.wins(state, Y)

    def get_empty_cells(self, state):
        return [[i, j]
                for i in range(3)
                for j in range(3)
                if state[i][j] in '_ ']

    def valid_move(self, state, i, j):
        return state[i][j] in '_ '

    def set_move(self, state, i, j, player):
        if self.valid_move(state, i, j):
            state[i][j] = player
            return True
        else:
            return False

    def minimax(self, state, depth, player, ai):
        if player == ai:
            best = [-1, -1, -inf]
        else:
            best = [-1, -1, +inf]

        if depth == 0 or self.game_over(state):
            score = self.evaluate(state, ai)
            return [-1, -1, score]

        for cell in self.get_empty_cells(state):
            i, j = cell[0], cell[1]
            state[i][j] = player
            score = self.minimax(state, depth - 1, other_char(player), ai)
            state[i][j] = ' '
            score[0], score[1] = i, j

            if player == ai:
                if score[2] > best[2]:
                    best = score
            else:
                if score[2] < best[2]:
                    best = score
        return best


class Field:
    H_SEP = '-' * 9

    def __init__(self) -> None:
        self.field = None
        self.gamer = {X: USER, Y: USER}

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

    def count(self, c: str) -> int:
        return len([y for x in self.field for y in x if y == c])

    def count_in_row(self, row: int, c: str) -> int:
        return len([y for y in range(3) if self.field[row][y] == c])

    def count_in_col(self, col: int, c: str) -> int:
        return len([x for x in range(3) if self.field[x][col] == c])

    def count_in_diag(self, main: bool, c: str) -> int:
        if main:
            return len([x for x in range(3) if self.field[x][x] == c])
        else:
            return len([x for x in range(3) if self.field[x][2 - x] == c])

    def is_row_win(self, i: int, c: str) -> bool:
        return self.count_in_row(i, c) == 3

    def is_col_win(self, j: int, c: str) -> bool:
        return self.count_in_col(j, c) == 3

    def is_diag_win(self, main: bool, c: str) -> bool:
        return self.count_in_diag(main, c) == 3

    def validate_field(self) -> str:
        empty_count = any(y for x in self.field for y in x if y == ' ')
        x_wins = 0
        y_wins = 0
        for i in range(3):
            if self.is_row_win(i, X):
                x_wins += 1
            if self.is_col_win(i, X):
                x_wins += 1
            if self.is_row_win(i, Y):
                y_wins += 1
            if self.is_col_win(i, Y):
                y_wins += 1
        if self.is_diag_win(True, X):
            x_wins += 1
        if self.is_diag_win(False, X):
            x_wins += 1
        if self.is_diag_win(True, Y):
            y_wins += 1
        if self.is_diag_win(False, Y):
            y_wins += 1

        if abs(self.count(X) - self.count(Y)) > 1 \
                or (x_wins > 0 and y_wins > 0):
            return "Impossible"
        elif x_wins > 0:
            return f"{X} wins"
        elif y_wins > 0:
            return f"{Y} wins"
        elif not empty_count:
            return "Draw"
        else:
            return ""

    def next_move(self, c: str):
        while True:
            if self.gamer[c] == USER:
                i, j = self.get_user_move()
            elif self.gamer[c] == EASY:
                print('Making move level "easy"')
                i, j = self.make_easy()
            elif self.gamer[c] == MEDIUM:
                print('Making move level "medium"')
                i, j = self.make_medium(c)
            elif self.gamer[c] == HARD:
                print('Making move level "hard"')
                i, j = self.make_hard(c)
            else:
                break
            self.field[i][j] = c
            self.print_field()
            break

    def get_user_move(self):
        i, j = 0, 0
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
            break
        return i, j

    def make_easy(self):
        i, j = 0, 0
        for ii in range(len(self.field)):
            done = False
            for jj in range(len(self.field[ii])):
                if self.field[ii][jj] in '_ ':
                    i = ii
                    j = jj
                    done = True
                    break
            if done:
                break
        return i, j

    def make_medium_get(self, c: str):
        for t in range(3):
            if self.count_in_row(t, c) == 2:
                for j in range(3):
                    if self.field[t][j] in '_ ':
                        return t, j
            elif self.count_in_col(t, c) == 2:
                for i in range(3):
                    if self.field[i][t] in '_ ':
                        return i, t
        if self.count_in_diag(True, c) == 2:
            for t in range(3):
                if self.field[t][t] in '_ ':
                    return t, t
        if self.count_in_diag(False, c) == 2:
            for t in range(3):
                if self.field[t][2 - t] in '_ ':
                    return t, 2 - t
        return None, None

    def make_medium(self, c: str):
        i, j = self.make_medium_get(c)
        if i is not None and j is not None:
            return i, j
        i, j = self.make_medium_get(other_char(c))
        if i is not None and j is not None:
            return i, j
        return self.make_easy()

    def make_hard(self, c: str):
        minimax = Minimax()
        depth = len(minimax.get_empty_cells(self.field))
        if depth == 0 or minimax.game_over(self.field):
            return None, None
        if depth == 9:
            i, j = self.make_easy()
        else:
            move = minimax.minimax(self.field, depth, c, c)
            i, j = move[0], move[1]
        return i, j

    def who_is_next(self) -> str:
        x_count = self.count(X)
        y_count = self.count(Y)
        return X if x_count == y_count else Y


possible_gamers = [USER, EASY, MEDIUM, HARD]
while True:
    cmd = input("Input command: ").strip().split()
    if cmd[0] == 'exit':
        break
    elif cmd[0] == 'start' \
            and len(cmd) >= 3 \
            and cmd[1] in possible_gamers \
            and cmd[2] in possible_gamers:
        pass
    else:
        print("Bad parameters!")
        continue
    f = Field()
    f.parse_field(' ' * 9)
    f.gamer[X] = cmd[1]
    f.gamer[Y] = cmd[2]
    # f.parse_field(input("Enter cells: "))
    f.print_field()
    while True:
        f.next_move(f.who_is_next())
        result = f.validate_field()
        if result:
            print(result)
            break
