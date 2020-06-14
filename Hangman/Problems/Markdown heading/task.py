def heading(s, level=1):
    if level < 1:
        level = 1
    if level > 6:
        level = 6
    return '#' * level + ' ' + s
