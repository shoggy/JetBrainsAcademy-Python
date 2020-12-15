def check(s: str):
    if s.isdigit():
        num = int(s)
        if num >= 202:
            print(num)
        else:
            print("There are less than 202 apples! You cheated on me!")
    else:
        print("It is not a number!")
