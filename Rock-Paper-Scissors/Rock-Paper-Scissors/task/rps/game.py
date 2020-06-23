import random

# Write your code here
shapes = ["rock", "paper", "scissors"]

user_name = input("Enter your name: ")
user_score = 0
print(f"Hello, {user_name}")

fin = open("rating.txt", mode="a+")
for lines in fin:
    name, score = lines.split()
    if name == user_name:
        user_score = int(score)
        break
fin.close()

options = input().strip()
if len(options) > 0:
    shapes = options.split(',')
mod = len(shapes)

print("Okay, let's start")

while True:
    user_input = input()
    if user_input == '!exit':
        print("Bye!")
        break
    if user_input == '!rating':
        print(f"Your rating: {user_score}")
        continue
    if user_input not in shapes:
        print("Invalid input")
        continue
    user_shape = shapes.index(user_input)
    ai_shape = random.randrange(0, mod)
    if user_shape == ai_shape:
        print(f"There is a draw ({shapes[ai_shape]})")
        user_score += 50
    # elif (ai_shape + 1) % len(shapes) == user_shape:
    elif (user_shape - ai_shape + mod) % mod <= mod // 2:
        print(f"Well done. Computer chose {shapes[ai_shape]} and failed")
        user_score += 100
    # elif (user_shape + 1) % mod == ai_shape:
    else:
        print(f"Sorry, but computer chose {shapes[ai_shape]}")
