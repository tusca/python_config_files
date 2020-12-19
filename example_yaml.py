#!/usr/bin/env python3
from yaml import load, dump
from pathlib import Path

input_path = Path('example.yaml')
text = input_path.read_text(encoding='utf8')

print('Content from file:')
print(text)
print('\n\n')

data = load(text)

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

output_text = dump(data)
output_path = Path('temp_example.yaml')
output_path.write_text(output_text, encoding='utf8')

print('Content written to new file:')
print(output_text)
print('\n\n')
