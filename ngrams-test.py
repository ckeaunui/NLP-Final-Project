# In order to apply methods such as Naive Bays to generate mood in text, let's first separate our text into unigrams.
import json
import os
import random
import nltk
from nltk import word_tokenize
from nltk import ngrams


def removePunctuation(wordFile):
    content = [w for w in wordFile if w.isalpha()]
    return content


all_text = []

for subdir, dirs, files in os.walk('json-scripts'):
    for i, file in enumerate(files):
        with open("json-scripts/" + str(file)) as f:
            data = json.load(f)
            for dictionary in data['movie_script']:
                if dictionary['type'] == 'speech':
                    char = dictionary['character']
                    dialogue = dictionary['text']
                    for word in word_tokenize(dialogue):
                        all_text.append(word.lower())


all_text = removePunctuation(all_text)

bigram_list = ngrams(all_text, 2)
trigram_list = ngrams(all_text, 3)

mega_list = []
mega_list += bigram_list
mega_list += trigram_list

cfd = nltk.ConditionalFreqDist([(tuple(a), b) for *a, b in mega_list])

word_list = [random.choice(all_text)]

for i in range(50):
    for i in range(2, 1, -1):
        if tuple(word_list[-i:]) in cfd:
            word_list.append(random.choice(list(cfd[tuple(word_list[-i:])].keys())))
            break
        else:
            continue

for word in word_list:
    print(word, end=" ")