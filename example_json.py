#!/usr/bin/env python3

from json import loads, dumps
from pathlib import Path

input_path = Path('example.json')
text = input_path.read_text(encoding='utf8')

print('Content from file:')
print(text)
print('\n\n')

data = loads(text)

print('Python data before change:')
print(data)
print('\n\n')

data['parameters'] = {
    'lifetime': '80s',
    'encoding': 'utf8',
    'duration_secs': 18
}
data['raws'] = [1, 8, 75, 94, 631]

print('Python data after change:')
print(data)
print('\n\n')

output_text = dumps(data, indent=4)
output_path = Path('temp_example.json')
output_path.write_text(output_text, encoding='utf8')

print('Content written to new file:')
print(output_text)
print('\n\n')
