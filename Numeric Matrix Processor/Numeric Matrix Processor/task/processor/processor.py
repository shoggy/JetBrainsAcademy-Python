from __future__ import annotations

ERROR = "The operation cannot be performed."


class Matrix:

    def __init__(self, row_num, col_num) -> None:
        self.n = row_num
        self.m = col_num
        self.a = None

    def read_matrix(self) -> None:
        self.a = list()
        for i in range(self.n):
            self.a.append([int(x) if x.isdigit() else float(x)
                           for x in input().split()])
            if len(self.a[i]) != self.m:
                print(ERROR)
                return

    def is_good(self) -> bool:
        return self.n is not None \
               and self.m is not None \
               and self.a is not None

    def __str__(self) -> str:
        if self.is_good():
            res = ''
            for row in self.a:
                for elem in row:
                    res += f"{elem} "
                res += '\n'
            return res

    def __add__(self, other: Matrix) -> Matrix:
        if self.n != other.n or self.m != other.m:
            print(ERROR)
            return Matrix(None, None)
        res = Matrix(self.n, self.m)
        res.a = list()
        for i in range(self.n):
            res.a.append([self.a[i][j] + other.a[i][j] for j in range(self.m)])
        return res

    def __mul__(self, other: float) -> Matrix:
        res = Matrix(self.n, self.m)
        res.a = list()
        for i in range(self.n):
            res.a.append([self.a[i][j] * other for j in range(self.m)])
        return res

    def mul(self, other: Matrix) -> Matrix:
        if self.m != other.n:
            print(ERROR)
            return Matrix(None, None)
        res = Matrix(self.n, other.m)
        res.a = list()
        for i in range(self.n):
            res.a.append(list())
            for j in range(other.m):
                dot = sum([self.a[i][k] * other.a[k][j] for k in range(self.m)])
                res.a[i].append(dot)
        return res

    def transpose_vertical(self) -> Matrix:
        res = Matrix(self.n, self.m)
        res.a = list()
        for row in self.a:
            res.a.append(row[::-1])
        return res

    def transpose_horizontal(self) -> Matrix:
        res = Matrix(self.n, self.m)
        res.a = self.a[::-1]
        return res

    def transpose_main(self) -> Matrix:
        res = Matrix(self.m, self.n)
        res.a = list()
        for i in range(self.m):
            res.a.append([self.a[k][i] for k in range(self.n)])
        return res

    def transpose_side(self) -> Matrix:
        res = Matrix(self.m, self.n)
        res.a = list()
        for i in range(-1, - self.m - 1, -1):
            res.a.append([self.a[k][i] for k in range(self.n)][::-1])
        return res

    def minor(self, i, j) -> Matrix:
        res = Matrix(self.n - 1, self.m - 1)
        res.a = list()
        for row in range(self.n):
            if row != i:
                res.a.append([self.a[row][col]
                              for col in range(self.m) if col != j])
        return res

    def c(self, i, j):
        return 1 if (i + j) % 2 == 0 else -1

    def determinant(self):
        if self.n == self.m == 1:
            return self.a[0][0]
        if self.n == self.m == 2:
            t = self.a
            return t[0][0] * t[1][1] - t[0][1] * t[1][0]
        res = 0
        for i in range(self.n):
            det = self.a[i][0] * self.minor(i, 0).determinant()
            res += self.c(i, 0) * det
        return res

    def inverse(self) -> Matrix:
        det = self.determinant()
        if det == 0:
            print("This matrix doesn't have an inverse.")
            return Matrix(None, None)
        adj = Matrix(self.n, self.m)
        adj.a = list()
        for i in range(self.n):
            adj.a.append(list())
            for j in range(self.m):
                c = self.c(i, j)
                determinant = self.minor(i, j).determinant()
                adj.a[i].append(c * determinant)
        return adj.transpose_main() * (1 / det)


def read_matrix_size(prompt):
    return (int(x) for x in input(prompt).split())


def user_input_matrix(name='') -> Matrix:
    if len(name) > 0:
        name += ' '
    mat = Matrix(*read_matrix_size(f"Enter size of {name}matrix: "))
    print(f"Enter {name}matrix:")
    mat.read_matrix()
    return mat


while True:
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    action = input("Your choice: ")
    if action == "0":
        break
    elif action == "1":
        a = user_input_matrix("first")
        b = user_input_matrix("second")
        c = a + b
        if c.is_good():
            print("The result is:")
            print(c)
    elif action == "2":
        a = user_input_matrix()
        d = float(input("Enter constant: "))
        e = a * d
        if e.is_good():
            print("The result is:")
            print(e)
    elif action == "3":
        a = user_input_matrix("first")
        b = user_input_matrix("second")
        c = a.mul(b)
        if c.is_good():
            print("The result is:")
            print(c)
    elif action == "4":
        print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        transpose_action = input("Your choice: ")
        a = user_input_matrix()
        b = a
        if transpose_action == "1":
            b = a.transpose_main()
        elif transpose_action == "2":
            b = a.transpose_side()
        elif transpose_action == "3":
            b = a.transpose_vertical()
        elif transpose_action == "4":
            b = a.transpose_horizontal()
        print("The result is:")
        print(b)
    elif action == "5":
        a = user_input_matrix()
        print("The result is:")
        print(a.determinant())
    elif action == "6":
        a = user_input_matrix()
        c = a.inverse()
        if c.is_good():
            print("The result is:")
            print(c)
