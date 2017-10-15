import telebot
import pickle
from logger import LOGGER
from textblob.classifiers import NaiveBayesClassifier
from text_processing import snowball_stemming, eliminate_low_feature_words, remove_punctuation

with open('network.pickle', 'rb') as handler:
    cl = pickle.load(handler)
bot = telebot.TeleBot('466512828:AAE-txqeXe4hAprU5hZvaDmBUJQsWoxIbJ8', threaded=False)

@bot.message_handler(func=lambda message: True)
def did_she_say(message):
    text = snowball_stemming(eliminate_low_feature_words(remove_punctuation(message.text.lower())))
    response = cl.prob_classify(text)
    LOGGER.info('"{}": {} {}'.format(message.text, round(response.prob('pos'), 2), round(response.prob('neg'), 2)))
    if response.prob('pos') > 0.83 and len(message.text.split()) > 2:
        bot.send_message(message.chat.id, "That's what she said.")

bot.polling(none_stop=True)
