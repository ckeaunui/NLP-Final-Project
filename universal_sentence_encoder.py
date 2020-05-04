import csv
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

model = hub.load("https://tfhub.dev/google/universal-sentence-encoder/4")
print("module loaded")

data = pd.read_csv('dialogue_data.csv')


def plot_similarity(labels, features, rotation):
    corr = np.inner(features, features)
    sns.set(font_scale=1.2)
    g = sns.heatmap(corr, \
                    xticklabels=labels, \
                    yticklabels=labels, \
                    vmin=0, \
                    vmax=1, \
                    cmap="YlGnBu")
    g.set_xticklabels(labels, rotation=rotation)
    g.set_title("Semantic Textual Similarity")
    plt.tight_layout()
    plt.savefig("semantic-similarity.png")
    plt.show()


character_lines = {}

# create dict of dialogue mapped to character
for row in data.itertuples():
    character_lines[row._1] = row.text

character_lines_encoded = []

# create custom labels using character names
character_labels = []

print("================================")
print("Characters found:")
for i in range(len(character_lines.keys())):
    print("{}: {}".format(i, list(character_lines.keys())[i]))
print("================================")
print("Enter character index to be used:")
print("Enter q or Q to stop.")
flag = True
char_index = ""
final_character_lines = {}
characters = list(character_lines.keys())
while flag:
    char_index = input()
    if char_index.upper() == 'Q':
        flag = False
    else:
        char_index = int(char_index)
        final_character_lines[characters[char_index]] = character_lines[characters[char_index]]

character_lines = final_character_lines

print("================================")
print("Characters selected:")
for i in range(len(character_lines.keys())):
    print("{}: {}".format(i, list(character_lines.keys())[i]))
print("================================")

for character in character_lines:
    character_labels.append(character)
    text = character_lines[character]
    character_lines_encoded.append(text)

# create matrix of all chosen character dialogue
embeddings_matrix = model(character_lines_encoded)
similarity_matrix = np.inner(embeddings_matrix, embeddings_matrix)

# plot matrix on heat map
plot_similarity(character_labels, embeddings_matrix, 90)
