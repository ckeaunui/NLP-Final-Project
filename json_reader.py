import json
import os
from nltk import word_tokenize


def add_character_speech(json_file, dictionary):
    # parses inputted JSON script, adding each character and their speech into a dictionary
    for block in json_file['movie_script']:
        if block['type'] == 'speech':
            character_name = block['character'].lower()

            # checks for screen directions or unnecessary additions in script
            # if present, removes them

            if '(' in character_name and ')' in character_name:
                start_index = character_name.find('(')
                end_index = character_name.find(')')
                character_name = character_name[:start_index-1]

            if character_name not in dictionary:
                dictionary[character_name] = word_tokenize(block['text'])
            else:
                dictionary[character_name] = dictionary[character_name] + word_tokenize(block['text'])


# with open("json-scripts/antz-JSON") as f:
#     data = json.load(f)

speech_by_character = {}

for subdir, dirs, files in os.walk('json-scripts'):
    for file in files:
        with open("json-scripts/" + str(file)) as f:
            data = json.load(f)
            add_character_speech(data, speech_by_character)

for character in speech_by_character:
    print(character)

print(speech_by_character['deckard'])