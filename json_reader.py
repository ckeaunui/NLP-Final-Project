import json
import os
import csv
import numpy as np
from nltk import *
import random
import nltk
import random
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords


def removeStopWords(wordFile):
    stopwordList = stopwords.words('english')
    content = [w for w in wordFile if w.lower() not in stopwordList]
    return content


def removePunctuation(wordFile):
    content = [w for w in wordFile if w.isalpha()]
    return content


# def stemWords(wordFile):
#     stemmer = PorterStemmer()
#     content = [stemmer.stem(w) for w in wordFile]
#     return content


def lemmatizeWords(wordFile):
    lemmatizer = WordNetLemmatizer()
    content = [lemmatizer.lemmatize(w) for w in wordFile]
    return content


def prepareText(wordFile):
    wordFile = removeStopWords(wordFile)
    wordFile = removePunctuation(wordFile)
    wordFile = np.char.lower(wordFile)
    wordFile = lemmatizeWords(wordFile)
    return wordFile


def add_character_speech(json_file, dictionary, name):
    # parses inputted JSON script, adding each character and their speech into a dictionary
    for block in json_file['movie_script']:
        if block['type'] == 'speech':
            character_name = block['character'].lower()

            # checks for screen directions or unnecessary additions in script
            # if present, removes them

            if '(' in character_name and ')' in character_name:
                start_index = character_name.find('(')
                character_name = character_name[:start_index - 1]

            if character_name not in dictionary[name]:
                dictionary[name][character_name] = word_tokenize(block['text'])
            else:
                dictionary[name][character_name] = dictionary[name][character_name] + word_tokenize(block['text'])


def make_csv(good_speech, bad_speech):
    row_list = []

    for character in good_speech:
        dialogue = good_speech[character]
        row_list.append([character, " ".join(dialogue), 0])

    for character in bad_speech:
        dialogue = bad_speech[character]
        row_list.append([character, " ".join(dialogue), 1])

    random.shuffle(row_list)

    with open('dialogue_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["character name", "text", "character role"])
        writer.writerows(row_list)


speech_by_character = {}

for subdir, dirs, files in os.walk('json-scripts'):
    for file in files:
        with open("json-scripts/" + str(file)) as f:
            data = json.load(f)
            film_name = str(file)[:-5]
            speech_by_character[film_name] = {}
            add_character_speech(data, speech_by_character, film_name)

for film in speech_by_character:
    print(film)
    for character in speech_by_character[film]:
        print("\t" + character)

print("Deckard speech: " + str(speech_by_character['blade-runner']['deckard']))

# adding protagonist speech
good_speech = {}
good_speech['deckard'] = (speech_by_character['blade-runner']['deckard'])
good_speech['z'] = (speech_by_character['antz']['z'])
good_speech['bourne'] = (speech_by_character['bourne-identity']['bourne'])
good_speech['steve'] = (speech_by_character['independence-day']['steve'])
good_speech['lydia'] = (speech_by_character['beetlejuice']['lydia'])
good_speech['somerset'] = (speech_by_character['seven']['somerset'])
good_speech['mills'] = (speech_by_character['seven']['mills'])
good_speech['red'] = (speech_by_character['shawshank-redemption']['red'])
good_speech['andy'] = (speech_by_character['shawshank-redemption']['andy'])
good_speech['truman'] = (speech_by_character['truman-show']['truman'])
good_speech['ripley'] = (speech_by_character['alien']['ripley'])
good_speech['woody'] = (speech_by_character['toy-story']['woody'])
good_speech['spiderman'] = (speech_by_character['spider-man']['spider-man'])
good_speech['neo'] = (speech_by_character['matrix']['neo'])
good_speech['morpheus'] = (speech_by_character['matrix']['morpheus'])
good_speech['batman'] = (speech_by_character['batman']['batman'])
good_speech['po'] = (speech_by_character['kung-fu-panda']['po'])

# adding antagonist speech
bad_speech = {}
bad_speech['betelgeuse'] = (speech_by_character['beetlejuice']['betelgeuse'])
bad_speech['mandible'] = (speech_by_character['antz']['mandible'])
bad_speech['roth'] = (speech_by_character['godfather-2']['roth'])
bad_speech['batty'] = (speech_by_character['blade-runner']['batty'])
bad_speech['conklin'] = (speech_by_character['bourne-identity']['conklin'])
bad_speech['john doe'] = (speech_by_character['seven']['john doe'])
bad_speech['norton'] = (speech_by_character['shawshank-redemption']['norton'])
bad_speech['bogs'] = (speech_by_character['shawshank-redemption']['bogs'])
bad_speech['travis'] = (speech_by_character['taxi-driver']['travis'])
bad_speech['christof'] = (speech_by_character['truman-show']['christof'])
bad_speech['agent smith'] = (speech_by_character['matrix']['agent smith'])
bad_speech['joker'] = (speech_by_character['batman']['joker'])

print("Deckard speech (stopwords, punctuation removed, lowercase, words lemmatized): " + str(good_speech['deckard']))
print("TRAVIS: " + str(bad_speech['travis']))

# this is what makes the CSV file!
# takes both lists and adds them to CSV in randomized order
make_csv(good_speech, bad_speech)