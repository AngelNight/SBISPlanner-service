import telebot


TOKEN = "277125289:AAEgpxzg5TXP81MXn-89pf2P8vXGlWtHVPQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)



bot.polling()