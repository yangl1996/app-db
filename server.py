__author__ = 'yangl1996'
from http.server import BaseHTTPRequestHandler, HTTPServer
import time

hostName = "128.199.244.33"
hostPort = 8080


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        user_id = self.path
        print(user_id)
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        self.wfile.write(bytes("<body><p>This is a test.</p>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))


myServer = HTTPServer((hostName, hostPort), MyServer)
print("Picture Server (beta) | Lei Yang i@yangl1996.com")
print(time.asctime(), "Picture Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Picture Server Stops - %s:%s" % (hostName, hostPort))