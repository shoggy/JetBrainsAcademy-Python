# write your code here
msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"


def get_num(s: str):
    try:
        return int(s)
    except ValueError:
        return float(s)


while True:
    print(msg_0)
    calc = input()
    [x, oper, y] = calc.split(' ')
    try:
        x = get_num(x)
        y = get_num(y)
    except ValueError:
        print(msg_1)
        continue
    if oper not in {'+', '-', '*', '/'}:
        print(msg_2)
    else:
        break
