import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

stemmer = SnowballStemmer("english")
def snowball_stemming(text):
    new_text = []
    for word in text.split():
        new_text.append(stemmer.stem(word))
    return ' '.join(new_text)

def eliminate_low_feature_words(text):
    text_set = set(text.split()) - (set(stopwords.words('english')) - {'she', 'her', 'herself', 'himself', 'he', 'him'})
    return ' '.join(text_set)

def remove_punctuation(text):
    for punctuation in [',', '.', '!', ':', ';', '/', '"']:
        text = text.replace(punctuation, '')
    return text.replace("'", ' ')
