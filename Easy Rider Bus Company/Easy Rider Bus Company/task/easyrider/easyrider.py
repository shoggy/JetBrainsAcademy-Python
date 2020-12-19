# Write your awesome code here
import json
from collections import defaultdict

stops_types = defaultdict(set)  # stop_type[SOF] => stop_name
bus_stops = defaultdict(list)  # bus_id => stop_type
stop_bus = defaultdict(list)
data = json.loads(input())

for bus in data:
    stops_types[bus['stop_type']].add(bus['stop_name'])
    bus_stops[bus['bus_id']].append(bus['stop_type'])
    stop_bus[bus['stop_name']].append(bus['bus_id'])

for bus, stop in bus_stops.items():
    if sum(1 for x in stop if x == 'S') != 1 or sum(1 for x in stop if x == 'F') != 1:
        print(f'There is no start or end stop for the line: {bus}.')
        exit()

transfers = {k: sorted(list(v)) for k, v in stop_bus.items() if len(v) > 1}
print(f'Start stops: {len(stops_types["S"])} {sorted(list(stops_types["S"]))}')
print(f'Transfer stops: {len(transfers)} {sorted(list(transfers.keys()))}')
print(f'Finish stops: {len(stops_types["F"])} {sorted(list(stops_types["F"]))}')
