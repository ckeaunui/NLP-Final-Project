# THIS IS A PRELIMINARY TEST OF RANDOM FOREST CLASSIFIER WITH CSV
# CHANGE TEST SIZE VARIABLE BELOW AS SIZE OF CSV IS INCREASED

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from subprocess import check_output

data = pd.read_csv('dialogue_data.csv')

X = data['text']
y = data['character role']

vectorizer = CountVectorizer()
vectorizer.fit(X)

X = vectorizer.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=101)

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

predictions = rfc.predict(X_test)
print(classification_report(y_test, predictions))

–––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––––

# THIS IS A PRELIMINARY TEST OF RANDOM FOREST CLASSIFIER WITH CSV
# CHANGE TEST SIZE VARIABLE BELOW AS SIZE OF CSV IS INCREASED

from sklearn.metrics import confusion_matrix, classification_report, accuracy_score
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
import pandas as pd
import numpy as np

data = pd.read_csv('dialogue_data.csv')

X = data['text']
y = data['character role']

vectorizer = CountVectorizer()
counts = vectorizer.fit_transform(X.values)
targets = y.values


classifier = MultinomialNB()
classifier.fit(counts, targets)

predictions = classifier.predict(counts)
print(classification_report(predictions, targets))
print(accuracy_score(predictions, targets))

user_input = pd.DataFrame(columns=['Input'])

#Add inputs in this format: ['Speech', 'Speech', etc.] for as many characters as you want.
#Include the full list of characters words for more accurate results
user_input['Input'] = ['']

v = vectorizer.transform(user_input['Input'].values)
print(classifier.predict(v))











