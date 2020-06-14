# Write your code here
import random


def get_masked_word(word: str, user_set: set) -> str:
    result = ''
    for c in word:
        result += (c if c in user_set else '-')
    return result


words = ['python', 'java', 'kotlin', 'javascript']

print("H A N G M A N")
while True:
    menu = input('Type "play" to play the game, "exit" to quit:')
    if menu != "play":
        break
        
    secret = random.choice(words)
    users_letters = set()

    attempts_left = 8
    while attempts_left > 0:
        print()
        masked_word = get_masked_word(secret, users_letters)
        print(masked_word)
        if '-' not in masked_word:
            print("You guessed the word!")
            print("You survived!")
            break
        letter = input("Input a letter: ")
        if len(letter) != 1:
            print("You should input a single letter")
        elif not (letter.isascii() and letter.islower()):
            print("It is not an ASCII lowercase letter")
        elif letter in users_letters:
            print("You already typed this letter")
        elif letter in secret:
            users_letters.add(letter)
        else:
            users_letters.add(letter)
            print("No such letter in the word")
            attempts_left -= 1
    else:
        print("You are hanged!")
