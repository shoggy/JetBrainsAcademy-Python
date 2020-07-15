# write your code here
import operator
from collections import deque

char_op = {'+': operator.add,
           '-': operator.sub,
           '*': operator.mul,
           '/': operator.floordiv,
           '^': operator.pow,
           '/-': operator.neg,
           '/+': operator.pos}

unary_op = {'/-', '/+'}

var_dict = dict()


class InvalidIdentifier(Exception):
    pass


class UnknownVariable(Exception):
    pass


def get_var(name: str) -> int:
    if name not in var_dict:
        raise UnknownVariable()
    nd = name
    while not isinstance(nd, int):
        nd = var_dict[nd]
        return nd


class Tokenizer:
    def __init__(self, s: str):
        self.s = s.strip()
        self.idx = 0
        self.prev = None

    def __str__(self):
        return f"Tokenizer({self.s[self.idx:]})"

    def has_next_token(self) -> bool:
        return self.idx < len(self.s)

    def next_token(self):
        while self.s[self.idx] == ' ':
            self.idx += 1
        if self.s[self.idx] in char_op or self.s[self.idx] in '()':
            res = self.s[self.idx]
            self.idx += 1
            if res in '+-' and (self.prev is None
                                or self.prev in char_op
                                or str(self.prev) in '()'):
                res = '/' + res
        else:
            idx2 = self.idx
            if self.s[idx2].isdigit():
                while idx2 < len(self.s) and self.s[idx2].isdigit():
                    idx2 += 1
                res = int(self.s[self.idx:idx2])
            else:
                while idx2 < len(self.s) and self.s[idx2].isalnum():
                    idx2 += 1
                res = self.s[self.idx:idx2]
                validate_var_name(res)
            self.idx = idx2
        self.prev = res
        return res


def validate_var_name(s: str):
    if not s.isalpha():
        raise InvalidIdentifier()


def process(s: str):
    if '=' in s:
        var_name, string = [x.strip() for x in s.split('=', 1)]
        try:
            validate_var_name(var_name)
            try:
                res = calculate_from_rpn(convert_to_rpn(string))
                var_dict[var_name] = res
            except UnknownVariable:
                print("Unknown variable")
            except:
                print("Invalid assignment")
        except InvalidIdentifier:
            print("Invalid identifier")
    else:
        try:
            res = calculate_from_rpn(convert_to_rpn(s))
            print(res)
        except InvalidIdentifier:
            print("Invalid identifier")
        except UnknownVariable:
            print("Unknown variable")
        except:
            print("Invalid expression")


def peek(queue: deque):
    t = queue.pop()
    queue.append(t)
    return t


def prec(c: str) -> int:
    if c in '()':
        return 0
    if c in '+-':
        return 6
    if c in '*/':
        return 8
    if c in unary_op:
        return 9
    if c in '^':
        return 9


def convert_to_rpn(s: str) -> deque:
    stack = deque()
    queue = deque()
    tokenizer = Tokenizer(s)
    while tokenizer.has_next_token():
        token = tokenizer.next_token()
        if isinstance(token, int) \
                or token not in char_op and token not in '()':
            queue.appendleft(token)
        elif token in unary_op:
            stack.append(token)
        elif token in char_op:
            while len(stack) > 0 and prec(token) <= prec(peek(stack)):
                queue.appendleft(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while len(stack) > 0 and peek(stack) != '(':
                queue.appendleft(stack.pop())
            stack.pop()
            # if stack becomes empty => parenthesis balance error
        else:
            raise Exception
    while len(stack) > 0:
        op = stack.pop()
        if op == '(':
            raise Exception
        queue.appendleft(op)
    return queue


def calculate_from_rpn(q: deque) -> int:
    stack = deque()
    while len(q) > 0:
        token = q.pop()
        if isinstance(token, int):
            stack.append(token)
        elif token not in char_op:
            stack.append(get_var(token))
        elif token in char_op:
            if token in unary_op:
                _a = stack.pop()
                stack.append(char_op[token](_a))
            else:
                _b = stack.pop()
                _a = stack.pop()
                stack.append(char_op[token](_a, _b))
    if len(stack) > 1:
        raise Exception
    return stack.pop()


while True:
    s = input().strip()
    if len(s) == 0:
        continue
    if s.startswith('/'):
        if s == "/exit":
            print("Bye!")
            break
        elif s == "/help":
            print("The program calculates the sum of numbers and difference *")
        else:
            print("Unknown command")
    else:
        process(s)
