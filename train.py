import numpy
import pickle
from textblob.classifiers import NaiveBayesClassifier
from text_processing import snowball_stemming, eliminate_low_feature_words, remove_punctuation

training_data = []
for data in ['positive', 'negative']:
    with open('data/{}.txt'.format(data), 'r', errors='replace', encoding='utf-8') as handler:
        for string in handler.read().splitlines():
            training_data.append((snowball_stemming(eliminate_low_feature_words(remove_punctuation(string.lower()))), data[0:3]))

training_data = numpy.array(training_data)

print('Starting training...')
cl = NaiveBayesClassifier(training_data)
cl.show_informative_features(10)

with open('network.pickle', 'wb') as handler:
    pickle.dump(cl, handler)
