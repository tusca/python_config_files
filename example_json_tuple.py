#!/usr/bin/env python3

from json import loads, dumps
from pathlib import Path
from collections import namedtuple
converter = lambda d: namedtuple('Example', d.keys())(*d.values())

input_path = Path('example.json')
text = input_path.read_text(encoding='utf8')

print('Content from file:')
print(text)
print('\n\n')

## --> Converter to convert from dict to tuple
data = loads(text, object_hook=converter)

print('Python structure')
print(data)

print('')
print('Individual fields accessed like objects')
print(data.database.user)
print(data.database.password)
print(data.database.server)
print(data.database.port)
print(data.api.url)
