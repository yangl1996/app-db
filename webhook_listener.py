from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import requests

listenAddr = "128.199.82.190"
listenPort = 9999


class MyServer(BaseHTTPRequestHandler):
    def do_POST(self):
        content_len = int(self.headers['content-length'])
        post_body = self.rfile.read(content_len).decode()
        self.send_response(200)
        self.end_headers()
        print(post_body)
        print("========END POST=========")



myServer = HTTPServer((listenAddr, listenPort), MyServer)
print("Webhook Listener")
print(time.asctime(), "Server Starts - %s:%s" % (listenAddr, listenPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Server Stops - %s:%s" % (listenAddr, listenPort))