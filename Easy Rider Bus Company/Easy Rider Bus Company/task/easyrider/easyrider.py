# Write your awesome code here
import json
from collections import defaultdict

bus_stops = defaultdict(dict)  # bus_id => stop_type
data = json.loads(input())

for bus in data:
    bus_stops[bus['bus_id']][bus['stop_id']] = bus

linear = dict()
for k, v in bus_stops.items():
    res = []
    stop = next(x for x in v.values() if x['stop_type'] == 'S')
    while stop['stop_type'] != 'F':
        res.append(stop)
        stop = v[stop['next_stop']]
    res.append(stop)
    linear[k] = res

print('Arrival time test:')
bad = False
for k, v in linear.items():
    m = "0"
    for x in v:
        if m >= x['a_time']:
            print(f'bus_id line {k}: wrong time on station {x["stop_name"]}')
            bad = True
            break
        else:
            m = x['a_time']
if not bad:
    print('OK')
