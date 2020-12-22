#!/usr/bin/env python3

from json import loads, dumps
from pathlib import Path

input_path = Path('example.json')
text = input_path.read_text(encoding='utf8')

class Database:
    def __init__(self, user, password, server, port):
        self.user = user
        self.password = password
        self.server = server
        self.port = port
    
class Config:
    def __init__(self, database, api):
        self.database = database
        self.api = api

class Factory:
    @staticmethod
    def create_database(obj):
        return Database(
            user=obj['user'],
            password=obj['password'],
            server=obj['server'],
            port=obj['port'],
        )

    @staticmethod
    def create_config(obj):
        return Config(
            database=Factory.create_database(obj['database']),
            api=obj['api']['url']
        )



print('Content from file:')
print(text)
print('\n\n')

data = Factory.create_config(loads(text))

print('Python structure')
print(data)

print('')
print('Individual fields accessed like objects ... IDEs can auto-complete and check fields:')
print(data.database.user)
print(data.database.password)
print(data.database.server)
print(data.database.port)
print(data.api)



