# use the function blackbox(lst) that is already defined
a = []
b = blackbox(a)
print("modifies" if a is b else "new")
