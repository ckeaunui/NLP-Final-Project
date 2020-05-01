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

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=101)

rfc = RandomForestClassifier()
rfc.fit(X_train, y_train)

predictions = rfc.predict(X_test)
print(classification_report(y_test, predictions))