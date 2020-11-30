from collections import defaultdict

transactions = [(38177, 34.38), (876, 999.99), (654276, 653678), (54366, 0.99),
                (546, 987.65), (876, 3456), (654276, 0.55), (38177, 876.75), (876, 98.7)]

# create transaction_dict
transaction_dict = defaultdict(list)
for transaction in transactions:
    transaction_dict[transaction[0]].append(transaction[1])
