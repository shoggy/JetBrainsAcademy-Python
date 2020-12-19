# Write your awesome code here
import collections
import json
import re


class FieldValidator:

    def __init__(self, name: str, mandatory: bool, t: type, validate) -> None:
        super().__init__()
        self.name = name
        self.mandatory = mandatory
        self.t = t
        self.validate = validate


fields = [
    FieldValidator('bus_id', True, int, lambda _: True),
    FieldValidator('stop_id', True, int, lambda _: True),
    FieldValidator('stop_name', True, str, lambda x: re.match(r'[A-Z].*(Road|Avenue|Boulevard|Street)$', x)),
    # FieldValidator('stop_name', True, str, lambda x: re.match(r'.+', x)),
    FieldValidator('next_stop', True, int, lambda _: True),
    FieldValidator('stop_type', False, str, lambda x: re.match(r'[SOF]?$', x)),
    FieldValidator('a_time', True, str, lambda x: re.match(r'(([01]\d)|(2[0-4])):[0-6]\d$', x)),
]


def validate(field: FieldValidator, bus) -> bool:
    if field.mandatory and field.name not in bus:
        return False
    if field.name in bus:
        attribute = bus[field.name]
        if not isinstance(attribute, field.t):
            return False
        if not field.validate(attribute):
            return False
    return True


errors = collections.Counter()

data = json.loads(input())
for bus in data:
    for field in fields:
        if not validate(field, bus):
            errors[field] += 1

print(f'Format validation: {sum(errors.values())} errors')
for field in fields:
    if field.t == str:
        print(f'{field.name}: {errors[field]}')
