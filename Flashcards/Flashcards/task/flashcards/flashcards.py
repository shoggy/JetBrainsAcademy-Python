# Write your code here
import io
import os
import random
import json


def log_print(s: str):
    log.write(s)
    log.write('\n')
    print(s)


def log_input(s='') -> str:
    log.write(s)
    user_input = input(s)
    log.write(user_input)
    return user_input


def add_card():
    term = log_input('The card:\n')
    while term in cards:
        log_print(f'The card "{term}" already exists.')
        term = log_input()
    definition = log_input('The definition of the card:\n')
    while definition in (x[0] for x in cards.values()):
        log_print(f'The definition "{definition}" already exists.')
        definition = log_input()
    cards[term] = (definition, 0)
    log_print(f'The pair ("{term}":"{definition}") has been added.')


def ask_cards():
    rev_dict = {v[0]: k for k, v in cards.items()}
    n = int(log_input('How many times to ask?\n'))
    for term, definition in random.choices(list((x[0], x[1][0]) for x in cards.items()), k=n):
        log_print(f'Print the definition of "{term}":')
        answer = log_input()
        if definition == answer:
            log_print('Correct!')
        else:
            cards[term] = (definition, cards[term][1] + 1)
            if answer in rev_dict:
                log_print(f'Wrong. The right answer is "{definition}", ' +
                          f'but your definition is correct for "{rev_dict[answer]}".')
            else:
                log_print(f'Wrong. The right answer is "{definition}".')


def remove_card():
    term = log_input('Which card?\n')
    if term in cards:
        cards.pop(term)
        log_print('The card has been removed.')
    else:
        log_print(f'Can\'t remove "{term}": there is no such card.')


def export_to():
    file_name = log_input('File name:\n')
    with open(file_name, mode='w', encoding='utf-8') as fout:
        json.dump(cards, fout)
        log_print(f'{len(cards)} cards have been saved.')


def import_from():
    file_name = log_input('File name:\n')
    if os.path.exists(file_name) and os.path.isfile(file_name) and os.access(file_name, os.R_OK):
        with open(file_name, mode='r', encoding='utf-8') as fin:
            imported = json.load(fin)
            cards.update(imported)
            log_print(f'{len(imported)} cards have been loaded.')
    else:
        log_print('File not found.')


def log_to_file():
    file_name = log_input('File name:\n')
    with open(file_name, mode='w', encoding='utf-8') as fout:
        fout.write(log.getvalue())
    log_print('The log has been saved.')


def hardest_card():
    m = max(x[1] for x in cards.values()) if cards else 0
    if m == 0:
        log_print('There are no cards with errors.')
    else:
        hardest_cards = ", ".join((f'"{k}"' for k, v in cards.items() if v[1] == m))
        log_print(f'The hardest card is {hardest_cards}. You have {m} errors answering it.')


def reset_stats():
    for k, v in cards.items():
        cards[k] = (v[0], 0)
    log_print('Card statistics have been reset.')


log = io.StringIO()
cards = dict()

while True:
    action = log_input('Input the action (add, remove, import, export, ask, exit, log, hardest card, reset stats):\n')
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
        log_print('Bye bye!')
        break
    elif action == 'log':
        log_to_file()
    elif action == 'hardest card':
        hardest_card()
    elif action == 'reset stats':
        reset_stats()
