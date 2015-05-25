__author__ = 'yangl1996'
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "128.199.244.33"
hostPort = 8080
db_file_path = "database.json"


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global db_file_path

        # parsing HTTP GET request
        user_id = self.path[1:]
        print("receiving request from ", self.client_address, " requesting user ", user_id)

        # looking up from database
        # data structure:{user_id_1: [url_1, url_2, url_3...], user_id_2: [url_1, url_2, url_3...]}

        # loading database
        database_file = open(db_file_path, 'r')
        database = database_file.read()
        user_table = json.loads(database)
        database_file.close()

        # database loaded as user_table
        # searching for URLs
        if user_id in user_table:
            URLs = user_table[user_id]
            # TODO: add XML generation

        else:
            # TODO: add error handling

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