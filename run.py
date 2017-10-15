import telebot
import pickle
from textblob.classifiers import NaiveBayesClassifier
from text_processing import snowball_stemming, eliminate_low_feature_words, remove_punctuation

with open('network.pickle', 'rb') as handler:
    cl = pickle.load(handler)
bot = telebot.TeleBot('466512828:AAE-txqeXe4hAprU5hZvaDmBUJQsWoxIbJ8')

@bot.message_handler(func=lambda message: True)
def did_she_say(message):
    text = snowball_stemming(eliminate_low_feature_words(remove_punctuation(message.text.lower())))
    response = cl.prob_classify(text)
    print('{}: {} {}'.format(message.text, response.prob('pos'), response.prob('neg')))
    if response.prob('pos') > 70 and len(message.text.split()) > 2:
        bot.send_message(message.chat.id, "That's what she said.")

bot.polling(none_stop=True)
