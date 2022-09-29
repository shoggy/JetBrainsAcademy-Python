# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_3 = "Yeah... division by zero. Smart move..."


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


while True:
    print(msg_0)
    calc = input()
    [x, oper, y] = calc.split(' ')
    x_num = 0
    y_num = 0
    try:
        x_num = get_num(x)
        y_num = get_num(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in {'+', '-', '*', '/'}:
        print(msg_2)
        continue
    try:
        res = operate(x_num, y_num, oper)
        print(res)
        break
    except ValueError:
        print(msg_3)
        continue
