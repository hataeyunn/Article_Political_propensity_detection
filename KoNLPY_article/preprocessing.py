import json
import nltk
import numpy as np

with open('train_docs.json') as f:
    train_docs = json.load(f)
with open('test_docs.json') as f:
    test_docs = json.load(f)

tokens = [t for d in train_docs for t in d[0]]
text = nltk.Text(tokens, name='capstone')

selected_words = [f[0] for f in text.vocab().most_common(10000)]

def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]

x_train = np.asarray(train_x).astype('float32')
x_test = np.asarray(test_x).astype('float32')

y_train = np.asarray(train_y).astype('float32')
y_test = np.asarray(test_y).astype('float32')

print("1")