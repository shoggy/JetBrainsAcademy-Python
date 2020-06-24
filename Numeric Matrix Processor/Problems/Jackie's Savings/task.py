def final_deposit_amount(*interest, amount=1000):
    res = amount
    for x in interest:
        res *= 1 + x / 100
    return round(res, 2)
