# Write your code here
import random
import os


def add_card():
    term = input('The card:\n')
    while term in cards:
        print(f'The card "{term}" already exists.')
        term = input()
    definition = input('The definition of the card:\n')
    while definition in cards.values():
        print(f'The definition "{definition}" already exists.')
        definition = input()
    cards[term] = definition
    print(f'The pair ("{term}":"{definition}") has been added.')


def ask_cards():
    rev_dict = {v: k for k, v in cards.items()}
    n = int(input('How many times to ask?\n'))
    for term, definition in random.choices(list(cards.items()), k=n):
        print(f'Print the definition of "{term}":')
        answer = input()
        if definition == answer:
            print('Correct!')
        elif answer in rev_dict:
            print(f'Wrong. The right answer is "{definition}", ' +
                  f'but your definition is correct for "{rev_dict[answer]}".')
        else:
            print(f'Wrong. The right answer is "{definition}".')


def remove_card():
    term = input('Which card?\n')
    if term in cards:
        cards.pop(term)
        print('The card has been removed.')
    else:
        print(f'Can\'t remove "{term}": there is no such card.')


def export_to():
    file_name = input('File name:\n')
    with open(file_name, mode='w', encoding='utf-8') as fout:
        fout.write(str(len(cards)) + '\n')
        for k, v in cards.items():
            fout.write(k + '\n')
            fout.write(v + '\n')
        print(f'{len(cards)} cards have been saved.')


def import_from():
    file_name = input('File name:\n')
    if os.path.exists(file_name) and os.path.isfile(file_name) and os.access(file_name, os.R_OK):
        with open(file_name, mode='r', encoding='utf-8') as fin:
            n = int(fin.readline())
            for _ in range(n):
                term = fin.readline()
                definition = fin.readline()
                cards[term] = definition
            print(f'{n} cards have been loaded.')
    else:
        print('File not found.')


cards = dict()

while True:
    action = input('Input the action (add, remove, import, export, ask, exit):\n')
    if action == 'add':
        add_card()
    elif action == 'remove':
        remove_card()
    elif action == 'import':
        import_from()
    elif action == 'export':
        export_to()
    elif action == 'ask':
        ask_cards()
    elif action == 'exit':
        print('Bye bye!')
        break
