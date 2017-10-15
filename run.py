import telebot
import pickle
from textblob.classifiers import NaiveBayesClassifier

cl = pickle.load(open('network.pickle', 'rb'))
bot = telebot.TeleBot('466512828:AAE-txqeXe4hAprU5hZvaDmBUJQsWoxIbJ8')

@bot.message_handler(func=lambda message: True)
def did_she_say(message):
    response = cl.prob_classify(message.text)
    if repsonse.prob('pos') > 70 and len(message.text.split(' ')) > 2:
        bot.send_message(message.chat.id, "That's what she said.")

bot.polling(none_stop=True)
