def price_string(func):
    def wrapper(arg):
        return '£' + str(func(arg))

    return wrapper


@price_string
def new_price(value):
    return float(value) * 0.9
