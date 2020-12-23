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

## load with namedtuple

[example_json_tuple.py](example_json_tuple.py)

allows to use the dots to access fields instead of brackets and quotes

## load with SimpleNamespace (new/shiny)

[example_json_simple.py](example_json_simple.py)

same but more python3-ish

## load 'manually' into class object

[example_json_object.py](example_json_object.py)

not only you have fields here but also IDEs will validate your use of valid fields and auto-complete and loading validates the expected structure

## dotty

TBD use the dotty module to allow single key to travel multiple levels deep into dicts

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


# Simple Ini
Only if you have no choice, right ?

```
from configparser import ConfigParser
config = ConfigParser()
config.read("/path/to/file.cfg")
with open("/path/to/file.cfg", "w") as f:
    config.write(f)
```

# Xml 
Who on earth would do that ?

# Todo

- add example with datetime serialization/deserialisation
- add dumps(d, default=str) example
