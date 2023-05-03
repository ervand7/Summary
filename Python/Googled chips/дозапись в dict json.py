import os
import json

example_file = '/Users/USER/Desktop/Ерванд. мусор/Новая папка3/json.json'

if not os.path.exists(example_file):
    first_file_record = {'k': 'v'}
    with open(example_file, mode='w', encoding='utf-8') as file:
        json.dump(first_file_record, file, ensure_ascii=False, indent=2)
else:
    with open(example_file, mode='r+', encoding='utf-8') as file:
        dictionary = json.load(file)
        dictionary['new_key'] = 'new_value'
        file.seek(0)
        json.dump(dictionary, file, ensure_ascii=False, indent=2)
        file.truncate()
