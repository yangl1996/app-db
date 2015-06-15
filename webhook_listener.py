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
        data = json.loads(post_body)
        if data['MediaType'] == 'image':
            user_id = data['Usr_Id']
            image_link = data['Pic_Url']
            print("New photo from %s, URL is %s." % (user_id, image_link))
        elif data['MediaType'] == 'voice':
            user_id = data['Usr_Id']
            media_id = data['Media_Id']
            print("New voice from %s, URL is %s." % (user_id, media_id))
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