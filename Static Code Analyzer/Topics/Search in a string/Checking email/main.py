def check_email(string: str):
    return ' ' not in string \
           and '@' in string \
           and string.find('.', string.index('@') + 2) > 0
