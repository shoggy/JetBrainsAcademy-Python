# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."
msg_4 = "Do you want to store the result? (y / n):"
msg_5 = "Do you want to continue calculations? (y / n):"
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"


def get_msg(i: int) -> str:
    return globals().get('msg_' + str(i))


def is_one_digit(v: float) -> bool:
    return -10 < v < 10 and v.is_integer()


def check(a, b, op):
    msg = ''
    if is_one_digit(a) and is_one_digit(b):
        msg = msg + msg_6
    if (a == 1 or b == 1) and op == '*':
        msg = msg + msg_7
    if (a == 0 or b == 0) and (op in {'*', '+', '-'}):
        msg = msg + msg_8
    if msg != '':
        msg = msg_9 + msg
        print(msg)


def get_num(s: str):
    return float(s)


def operate(a, b, op: str):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    elif op == '/' and b:
        return a / b
    else:
        raise ValueError("bad args")


def ask(question: str) -> bool:
    while True:
        print(question)
        answer = input()
        if answer == 'y':
            return True
        elif answer == 'n':
            return False


def ask_to_store(res: float) -> bool:
    if ask(msg_4):
        if not is_one_digit(res):
            return True
        msg_index = 10
        while True:
            print(get_msg(msg_index))
            answer = input()
            if answer == 'y':
                if msg_index < 12:
                    msg_index += 1
                    continue
                else:
                    return True
            elif answer == 'n':
                return False


def ask_to_continue() -> bool:
    return ask(msg_5)


memory = 0
while True:
    print(msg_0)
    calc = input()
    [x, oper, y] = calc.split(' ')
    x_num = 0
    y_num = 0
    if x == 'M':
        x = memory
    if y == 'M':
        y = memory
    try:
        x_num = get_num(x)
        y_num = get_num(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in {'+', '-', '*', '/'}:
        print(msg_2)
        continue
    check(x_num, y_num, oper)
    try:
        res = operate(x_num, y_num, oper)
    except ValueError:
        print(msg_3)
        continue
    print(res)
    if ask_to_store(res):
        memory = res
    if ask_to_continue():
        continue
    else:
        break
