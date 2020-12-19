# Write your awesome code here
import collections
import json

stops = collections.Counter()
data = json.loads(input())

for bus in data:
    stops[bus['bus_id']] += 1

print('Line names and number of stops:')
for k, v in stops.items():
    print(f'bus_id: {k}, stops: {v}')
