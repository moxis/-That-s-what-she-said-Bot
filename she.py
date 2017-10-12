import telebot
from random import randint

trigger_words = {
'long': ['long', 'deep', 'lengthy', 'enlarged', 'elongate', 'lasting', 'lasted'],
'short': ['short', 'little', 'small', 'flaccid', 'microscopic', 'miniature', 'minuscule', 'mini'],
'hard': ['hard', 'solid', 'rough', 'harsh', 'tough', 'gentle'],
'thick': ['thick'],
'fast': ['fast', 'rapid', 'quick', 'agile', 'swift', 'hot'],
'come': ['come', 'coming', 'enter', 'go in'],
'big': ['big', 'colossal', 'enormous', 'gigantic', 'massive', 'substantial', 'tremendous', 'huge'],
'wet': ['wet', 'moist', 'slippery', 'soak', 'dry'],
}

bot = telebot.TeleBot('466512828:AAE-txqeXe4hAprU5hZvaDmBUJQsWoxIbJ8')

@bot.message_handler(func=lambda message: True)
def she_says(message):
    for category in trigger_words:
        for word in trigger_words[category]:
            if word in message.text.lower():
                bot.send_message(message.chat.id, "That's what she said!")
                break
        else:
            continue
        break

bot.polling(none_stop=True)
