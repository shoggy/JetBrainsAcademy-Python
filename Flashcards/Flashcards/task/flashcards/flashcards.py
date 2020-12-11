# Write your code here

class Card:

    def __init__(self, term, definition) -> None:
        super().__init__()
        self.term = term
        self.definition = definition


cards_list = []
n = int(input('Input the number of cards:\n'))
for i in range(1, n + 1):
    term = input(f'The term for card #{i}:\n')
    while any(x for x in cards_list if x.term == term):
        term = input(f'The term "{term}" already exists. Try again:\n')
    definition = input(f'The definition for card #{i}:\n')
    while any(x for x in cards_list if x.definition == definition):
        definition = input(f'The definition "{definition}" already exists. Try again:\n')
    card = Card(term, definition)
    cards_list.append(card)

rev_dict = {x.definition: x.term for x in cards_list}
for card in cards_list:
    print(f'Print the definition of "{card.term}":')
    answer = input()
    if card.definition == answer:
        print('Correct!')
    elif answer in rev_dict:
        print(f'Wrong. The right answer is "{card.definition}", ' +
              f'but your definition is correct for "{rev_dict[answer]}".')
    else:
        print(f'Wrong. The right answer is "{card.definition}".')
