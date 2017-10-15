import numpy
import pickle
from textblob.classifiers import NaiveBayesClassifier

training_data = []

with open('data/positive.txt', 'r', errors='replace', encoding='utf-8') as positive:
    for funny in positive.read().splitlines():
        training_data.append((funny, 'pos'))

with open('data/negative.txt', 'r', errors='replace', encoding='utf-8') as negative:
    for lame in negative.read().splitlines():
        training_data.append((lame, 'neg'))

training_data = numpy.array(training_data)
print('Starting training...')
cl = NaiveBayesClassifier(training_data)

with open('network.pickle', 'wb') as handler:
    pickle.dump(cl, handler, protocol=pickle.HIGHEST_PROTOCOL)
