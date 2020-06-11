income = int(input())
percent = 0
if income < 15_528:
    percent = 0
elif income < 42_708:
    percent = 15
elif income < 132_407:
    percent = 25
else:
    percent = 28
tax = income * percent / 100
print(f'The tax for {income} is {percent}%. That is {tax:.0f} dollars!')
