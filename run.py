import telebot
import pickle
from logger import LOGGER
from textblob.classifiers import NaiveBayesClassifier
from text_processing import snowball_stemming, eliminate_low_feature_words, remove_punctuation

with open('network.pickle', 'rb') as handler:
    cl = pickle.load(handler)
bot = telebot.TeleBot('466512828:AAE-txqeXe4hAprU5hZvaDmBUJQsWoxIbJ8', threaded=False)

@bot.message_handler(func=lambda message: message.reply_to_message is None)
def did_she_say(message):
    text = snowball_stemming(remove_punctuation(message.text.lower()))
    response = cl.prob_classify(text)
    LOGGER.info('"{}": {} {}'.format(message.text, round(response.prob('pos'), 2), round(response.prob('neg'), 2)))
    if response.prob('pos') > 0.92 and len(message.text.split()) > 2:
        bot.send_message(message.chat.id, "That's what she said!")

@bot.message_handler(func=lambda message: message.reply_to_message is not None and 'stat' in message.text.lower())
def return_statistics(message):
    text = snowball_stemming(remove_punctuation(message.reply_to_message.text.lower()))
    response = cl.prob_classify(text)
    bot.send_message(message.chat.id, 'I am *{}%* certain that she said this!'.format(round(response.prob('pos')*100, 2)), parse_mode='Markdown')

@bot.message_handler(func=lambda message: message.reply_to_message is not None and message.text.lower() in ['bad bot', 'good bot'])
def retrain(message):
    if message.text == 'bad bot':
        mode = 'neg'
    else:
        mode = 'pos'
    text = snowball_stemming(remove_punctuation(message.reply_to_message.text.lower()))
    cl.update([(text, mode) for x in range(0, 10)])
    with open('network.pickle', 'wb') as handler:
        pickle.dump(cl, handler)
    bot.send_message(message.chat.id, '`RETRAINED! ALWAYS LEARNING FROM MY MISTAKES`', parse_mode='Markdown')

bot.polling(none_stop=True)
