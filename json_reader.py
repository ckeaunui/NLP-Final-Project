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
        dialogue = prepareText(good_speech[character])
        row_list.append([character, " ".join(dialogue), 0])

    for character in bad_speech:
        dialogue = prepareText(bad_speech[character])
        row_list.append([character, " ".join(dialogue), 1])

    random.shuffle(row_list)

    with open('dialogue_data.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["character name", "text", "character role"])
        writer.writerows(row_list)


speech_by_character = {}

for subdir, dirs, files in os.walk('json-scripts'):
    for i, file in enumerate(files):
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
good_speech['ambrose'] = speech_by_character['the-birds']['ambrose']
good_speech['ethan'] = speech_by_character['mission-impossible-2']['ethan']
good_speech['joey donner'] = speech_by_character['the-proposal']['joey donner']
good_speech['cameron'] = speech_by_character['ten-things-i-hate-about-you']['cameron']
good_speech['kat'] = speech_by_character['ten-things-i-hate-about-you']['kat']
good_speech['grady'] = speech_by_character['wonder-boys']['grady']
good_speech['steed'] = speech_by_character['the-avengers']['steed']
good_speech['emma'] = speech_by_character['the-avengers']['emma']
good_speech['bailey'] = speech_by_character['the-avengers']['bailey']
good_speech['mother'] = speech_by_character['the-avengers']['mother']
good_speech['nadia'] = speech_by_character['american-pie']['nadia']
good_speech['finch'] = speech_by_character['american-pie']['finch']
good_speech['jim'] = speech_by_character['american-pie']['jim']
good_speech['stifler\'s mom'] = speech_by_character['american-pie']['stifler\'s mom']
good_speech['sherman'] = speech_by_character['american-pie']['sherman']
good_speech['vicky'] = speech_by_character['american-pie']['vicky']
good_speech['michelle'] = speech_by_character['american-pie']['michelle']
good_speech['jim\'s dad'] = speech_by_character['american-pie']['jim\'s dad']
good_speech['kevin'] = speech_by_character['american-pie']['kevin']
good_speech['heather'] = speech_by_character['american-pie']['heather']
good_speech['deckard'] = speech_by_character['blade-runner']['deckard']
good_speech['z'] = speech_by_character['antz']['z']
good_speech['bourne'] = speech_by_character['bourne-identity']['bourne']
good_speech['steve'] = speech_by_character['independence-day']['steve']
good_speech['lydia'] = speech_by_character['beetlejuice']['lydia']
good_speech['somerset'] = speech_by_character['seven']['somerset']
good_speech['mills'] = speech_by_character['seven']['mills']
good_speech['red'] = speech_by_character['shawshank-redemption']['red']
good_speech['andy dufresne'] = speech_by_character['shawshank-redemption']['andy']
good_speech['truman'] = speech_by_character['truman-show']['truman']
good_speech['ripley'] = speech_by_character['alien']['ripley']
good_speech['woody'] = speech_by_character['toy-story']['woody']
good_speech['spiderman'] = speech_by_character['spider-man']['spider-man']
good_speech['peter parker'] = speech_by_character['spider-man']['peter']
good_speech['flash'] = speech_by_character['spider-man']['flash']
good_speech['neo'] = speech_by_character['matrix']['neo']
good_speech['morpheus'] = speech_by_character['matrix']['morpheus']
good_speech['batman'] = speech_by_character['batman']['batman']
good_speech['po'] = speech_by_character['kung-fu-panda']['po']
good_speech['bruce wayne'] = speech_by_character['batman']['bruce wayne']
good_speech['joel'] = speech_by_character['eternal-sunshine']['joel']
good_speech['clementine'] = speech_by_character['eternal-sunshine']['clementine']
good_speech['caleb'] = speech_by_character['ex-machina']['caleb']
good_speech['shifu'] = speech_by_character['kung-fu-panda']['shifu']
good_speech['bob'] = speech_by_character['lost-in-translation']['bob']
good_speech['charlotte'] = speech_by_character['lost-in-translation']['charlotte']
good_speech['monica'] = speech_by_character['love-and-basketball']['monica']
good_speech['quincy'] = speech_by_character['love-and-basketball']['quincy']
good_speech['morpheus'] = speech_by_character['matrix']['morpheus']
good_speech['billy'] = speech_by_character['midnight-express']['billy']
good_speech['ethan hunt'] = speech_by_character['mission-impossible']['ethan']
good_speech['luke'] = speech_by_character['new-hope']['luke']
good_speech['leia'] = speech_by_character['new-hope']['leia']
good_speech['sarah conners'] = speech_by_character['terminator']['sarah']
good_speech['buzz lightyear'] = speech_by_character['toy-story']['buzz']
good_speech['keating'] = speech_by_character['dead-poets-society']['keating']
good_speech['mater'] = speech_by_character['cars-2']['mater']
good_speech['lucy pevensie'] = speech_by_character['narnia']['lucy']
good_speech['shrek'] = speech_by_character['shrek-3']['shrek']
good_speech['roger rabbit'] = speech_by_character['who-shot-roger-rabbit']['roger rabbit']
good_speech['adam'] = speech_by_character['5050']['adam']
good_speech['josie'] = speech_by_character['never-been-kissed']['josie']
good_speech['aldys'] = speech_by_character['never-been-kissed']['aldys']
good_speech['enid'] = speech_by_character['ghost-world']['enid']
good_speech['ichabod'] = speech_by_character['sleepy-hollow']['ichabod']

# adding antagonist speech
bad_speech = {}
bad_speech['ambrose'] = speech_by_character['mission-impossible-2']['ambrose']
bad_speech['joey'] = speech_by_character['ten-things-i-hate-about-you']['joey']
bad_speech['ed'] = speech_by_character['the-man-who-wasnt-there']['ed']
bad_speech['dave'] = speech_by_character['the-man-who-wasnt-there']['dave']
bad_speech['walter gaskell'] = speech_by_character['wonder-boys']['walter gaskell']
bad_speech['steve stifler'] = speech_by_character['']['']
bad_speech['betelgeuse'] = speech_by_character['beetlejuice']['betelgeuse']
bad_speech['mandible'] = speech_by_character['antz']['mandible']
bad_speech['roth'] = speech_by_character['godfather-2']['roth']
bad_speech['batty'] = speech_by_character['blade-runner']['batty']
bad_speech['conklin'] = speech_by_character['bourne-identity']['conklin']
bad_speech['john doe'] = speech_by_character['seven']['john doe']
bad_speech['norton'] = speech_by_character['shawshank-redemption']['norton']
bad_speech['bogs'] = speech_by_character['shawshank-redemption']['bogs']
bad_speech['travis'] = speech_by_character['taxi-driver']['travis']
bad_speech['christof'] = speech_by_character['truman-show']['christof']
bad_speech['agent smith'] = speech_by_character['matrix']['agent smith']
bad_speech['joker'] = speech_by_character['batman']['joker']
bad_speech['vader'] = speech_by_character['new-hope']['vader']
bad_speech['nathan'] = speech_by_character['ex-machina']['nathan']
bad_speech['jason'] = speech_by_character['friday-the-13th-VIII']['jason']
bad_speech['tai lung'] = speech_by_character['kung-fu-panda']['tai lung']
bad_speech['hamidou'] = speech_by_character['midnight-express']['hamidou']
bad_speech['phelps'] = speech_by_character['mission-impossible']['phelps']
bad_speech['ock'] = speech_by_character['spider-man']['ock']
bad_speech['terminator'] = speech_by_character['terminator']['terminator']
bad_speech['jack torrance'] = speech_by_character['the-shining']['jack']
bad_speech['sid'] = speech_by_character['toy-story']['sid']
bad_speech['mr nolan'] = speech_by_character['dead-poets-society']['mr nolan']
bad_speech['professor zundapp'] = speech_by_character['cars-2']['professor zundapp']
bad_speech['miles axlerod'] = speech_by_character['cars-2']['miles axlerod']
bad_speech['hannibal lecter'] = speech_by_character['hannibal']['hannibal']
bad_speech['jason dean'] = speech_by_character['heathers']['jason']
bad_speech['white witch'] = speech_by_character['narnia']['white witch']
bad_speech['rumplestiltskin'] = speech_by_character['shrek-3']['rumplestiltskin']
bad_speech['judge doom'] = speech_by_character['who-shot-roger-rabbit']['doom']
bad_speech['kirsten'] = speech_by_character['never-been-kissed']['kirsten']
bad_speech['gibby'] = speech_by_character['never-been-kissed']['gibby']
bad_speech['kristen'] = speech_by_character['never-been-kissed']['kristen']
bad_speech['roberta'] = speech_by_character['ghost-world']['roberta']
bad_speech['brom'] = speech_by_character['sleepy-hollow']['brom']
bad_speech['lady van tassel'] = speech_by_character['sleepy-hollow']['lady van tassel']

print("Deckard speech (stopwords, punctuation removed, lowercase, words lemmatized): " + str(good_speech['deckard']))
print("TRAVIS: " + str(bad_speech['travis']))

# this is what makes the CSV file!
# takes both lists and adds them to CSV in randomized order
make_csv(good_speech, bad_speech)
