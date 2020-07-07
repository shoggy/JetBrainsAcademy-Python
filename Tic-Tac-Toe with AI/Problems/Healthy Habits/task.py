import statistics

# the list "walks" is already defined
# your code here
print(round(statistics.mean([x["distance"] for x in walks])))
