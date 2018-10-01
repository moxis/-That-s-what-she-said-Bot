# TWSS BOT

Telegram chatbot that uses Naive Bayes Probability Theorem to reply with "That's what she said!" at certain moments! 

### Prerequisites
* Python 3+

Install these modules through pip:

```
$ pip install pyTelegramBotAPI
$ pip install textblob
$ pip install numpy
$ pip install nltk
```

### Installing

Before starting anything we need to train our model. You can edit the text files in data folder with your own data before training. Simply execute train.py to start training. This can take a while and will use up a LOT of RAM. If your RAM is insufficient I suggest reducing the data size. 

```
$ python train.py
```

Afterwards, change the token in run.py to your token of choice and execute run.py to start the bot.

```
$ python run.py
```

That's it! Now you can interact with your hilarious bot. You can add this into group chats for extra fun.

## Example
You can view the probability by replying to the phrase with "stats"

![Example](https://i.imgur.com/1NcilGq.png)

You can easily retrain your bot to prevent certain phrases by replying "bad bot"

![Retraining Example](https://i.imgur.com/1S36p64.png)

