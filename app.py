## -*- coding: utf-8 -*-
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import telebot

hostName = "localhost"
hostPort = 80


TOKEN = "277125289:AAEgpxzg5TXP81MXn-89pf2P8vXGlWtHVPQ"
bot = telebot.TeleBot(TOKEN)


def request_pars(str):
    #str.replace('/', '')
    #str[0] = ''
    str = str[1:]
    l = str.split('%')


    #print(len(l))

        #bot.send_message(TOKEN, l[1], l[2])
    print(l)
    if l[1] == "new-task":
            bot.send_message(221482003, "У вас новое задание" + "\n" + l[2], )
    elif l[1] == "close-task":
            bot.send_message(221482003, "Вам нужно закрыть задачу" + "\n" + l[2])
    elif l[1] == "conference":
            bot.send_message(221482003, "Вас приглошают на совещание" + "\n" + l[2])
    elif l[1] == "calendar":
            bot.send_message(221482003, "Ваше расписание составлено" + "\n" + l[2])

    return l

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        #print(self.path)
        request_pars(self.path)
        #if self.path == "stop":
        #    myServer.server_close()



myServer = HTTPServer((hostName, hostPort), MyServer)
print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))


try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

#import telebot


#TOKEN = "277125289:AAEgpxzg5TXP81MXn-89pf2P8vXGlWtHVPQ"

#bot = telebot.TeleBot(TOKEN)

#@bot.message_handler(commands=['start', 'help'])
#def send_welcome(message):
#    bot.reply_to(message, "Howdy, how are you doing?")

#@bot.message_handler(func=lambda message: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)



#bot.polling()

#def wsgi_app(environ, start_response):
#    status = '200 OK'
#    response_headers = [('Content-type', 'text/plain')]
#    start_response(status, response_headers)
#    response_body = 'Hello World'
#    yield response_body.encode()

#if __name__ == '__main__':
#    from wsgiref.simple_server import make_server

#    httpd = make_server('localhost', 80, wsgi_app)
#    httpd.serve_forever()