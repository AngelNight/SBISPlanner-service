import telebot


def wsgi_app(environ, start_response):
    status = '200 OK'
    response_headers = [('Content-type', 'text/plain')]
    start_response(status, response_headers)
    response_body = 'Hello World'
    yield response_body.encode()



if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 80, wsgi_app)
    httpd.serve_forever()

def sendMessage(msg, author_exists=True):
   return True

TOKEN = "277125289:AAEgpxzg5TXP81MXn-89pf2P8vXGlWtHVPQ"
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(massage):
    bot.reply_to(massage, "QWE!!1")


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling(True)





