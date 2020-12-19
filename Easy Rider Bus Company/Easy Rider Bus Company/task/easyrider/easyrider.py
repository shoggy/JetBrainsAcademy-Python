# Write your awesome code here
import json
from collections import defaultdict

stops_types = defaultdict(set)
stop_bus = defaultdict(list)
data = json.loads(input())

for bus in data:
    stops_types[bus['stop_type']].add(bus['stop_name'])
    stop_bus[bus['stop_name']].append(bus['bus_id'])

start_stops = stops_types["S"]
final_stops = stops_types["F"]
transfers = {k for k, v in stop_bus.items() if len(v) > 1}

errors = sorted(x for x in stops_types["O"] if x in start_stops or x in final_stops or x in transfers)

print('On demand stops test:')
if errors:
    print(f'Wrong stop type: {errors}')
else:
    print('OK')
