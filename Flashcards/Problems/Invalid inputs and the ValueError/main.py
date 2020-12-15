def check():
    s = input()
    if s.isdigit() and 25 <= int(s) <= 37:
        print(s)
    else:
        print("Correct the error!")
