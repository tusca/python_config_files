# python_config_files

Examples of reading/writing sorts of configuration files.

Feel free to get some inpiration, those are far from perfect and can always be improved upon.

PS: I'm a big fan of pathlib therefore I use it here ;-)

# requirements

- python3

## installation

`pip install -r requirements.txt` or `python -m pip install -r requirements.txt` to install required modules

# Json
Anything goes ;-)
## required modules
none
## essentials

```
from json import loads, dumps

# loads to convert text to data
# dumps to convert data to text
```

PS: other functions exist ...

## Source code

[example_json.py](example_json.py)

# Yaml
Mostly for simple structures
## required modules
- pyyaml -> https://pyyaml.org/wiki/PyYAMLDocumentation

## essentials

```
from yaml import load, dump
```

## Source code

[example_yaml.py](example_yaml.py)

# Ini
Only if you have no choice ?

# Xml 
Who on earth would do that ?

# Todo

- add example with datetime serialization/deserialisation
- add dumps(d, default=str) example
