# Write your code here

class Card:

    def __init__(self, term, definition) -> None:
        super().__init__()
        self.term = term
        self.definition = definition


cards_list = []
n = int(input('Input the number of cards:\n'))
for i in range(1, n + 1):
    card = Card(input(f'The term for card #{i}:\n'),
                input(f'The definition for card #{i}:\n'))
    cards_list.append(card)

for card in cards_list:
    print(f'Print the definition of "{card.term}":')
    answer = input()
    if card.definition == answer:
        print('Correct!')
    else:
        print(f'Wrong. The right answer is "{card.definition}".')
