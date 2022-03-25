import telebot

with open ("bot_token", "r") as myfile:
    bot_token=myfile.readlines()

token = bot_token[0]

bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text"])
def echo(message):
    bot.send_message(message.chat.id, message.text)

bot.polling(none_stop=True)