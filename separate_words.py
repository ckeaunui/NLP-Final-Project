#In order to apply methods such as Naive Bays to generate mood in text, let's first separate our text into unigrams.
import json


def clean (string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    no_punct = ""
    for char in string:
        if char not in punctuations:
            no_punct = no_punct + char
    return no_punct

def ngrams(input, n):         #this is currently not in use
   input = input.split(' ')
   output = {}
   for i in range(len(input)-n+1):
       g = ' '.join(input[i:i+n])
       output.setdefault(g, 0)
       output[g] += 1
       return output

# def clean_dict(dictionary):
#     for k, v in dictionary.items():
#         dictionary[k] = clean(v)
#     return dictionary

character_says = {}
with open('/Users/jasmine/PycharmProjects/NLP-Final-Project/json-scripts/5050-JSON.json') as json_data:
    data_dict = json.load(json_data)
    for dictionary in data_dict['movie_script']:
        if dictionary['type'] == 'speech':
            char = dictionary['character']
            dialogue = dictionary['text']
            character_says[char] = dialogue

#character_says dictionary has character, dialogue pairings

#clean the dictionary dialogue
for k, v in character_says.items():
    character_says[k] = clean(v)
    character_says[k] = character_says[k].rstrip("\n")
    character_says[k] = (character_says[k].split(' '))

print(character_says)

