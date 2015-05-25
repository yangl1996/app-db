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
        try:
            database_file = open(db_file_path, 'r')
            database = database_file.read()
            user_table = json.loads(database)
            database_file.close()
        except:
            self.send_error(500, "Internal Error", "No database found on server")
            print("Database not found, server shutting down")
            return

        # database loaded as user_table
        # searching for URLs
        if user_id in user_table:
            URLs = user_table[user_id]
            return_file = '<resources><string name="url_number">'
            return_file += len(URLs)
            return_file += '</string>'
            id_count = 1
            for this_url in URLs:
                return_file += '<string name="'
                return_file += id_count
                return_file += '">'
                return_file += this_url
                return_file += '</string>'
            return_file += '</resources>'
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(return_file, "utf-8"))
        else:
            self.send_error(404, "Not Found", "The username you requested does not exist")


myServer = HTTPServer((hostName, hostPort), MyServer)
print("Picture Server (beta) | Lei Yang i@yangl1996.com")
print(time.asctime(), "Picture Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Picture Server Stops - %s:%s" % (hostName, hostPort))