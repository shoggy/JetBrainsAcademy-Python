# write your code here
with open("users.json", "r") as fin:
    obj = json.load(fin)
    print(len(obj['users']))
