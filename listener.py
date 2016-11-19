from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import telebot

hostName = "localhost"
hostPort = 8000


TOKEN = "277125289:AAEgpxzg5TXP81MXn-89pf2P8vXGlWtHVPQ"
bot = telebot.TeleBot(TOKEN)


def request_pars(str):
    #str.replace('/', '')
    #str[0] = ''
    l = str.split('/')


    #print(len(l))
    if len(l) == 3 :
        #bot.send_message(TOKEN, l[1], l[2])
        bot.send_message(l[1], l[2])
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



