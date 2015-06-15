__author__ = 'yangl1996'
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json

hostName = "128.199.82.190"
hostPort = 8080
db_file_path = "database.json"


class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        global db_file_path

        # parsing HTTP GET request
        user_id = self.path[1:]
        print("receiving request from ", self.client_address, " requesting user ", user_id)

        # looking up from database

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
        if user_id == "get":
            album = user_table['image']
            return_file = '<resources>'
            for instance in album:
                return_file += """<photo>
                <imgUrl>{imageURL}</imgUrl>
                <audioUrl>{audioURL}</audioUrl>
                <words>{text}</words>
                <name>{usrid}</name>
                </photo>""".format(imageURL=instance['url'], text=instance['text'], usrid=instance['name'],
                                   audioURL=instance['audio'])
            return_file += '</resources>'
            self.send_response(200)
            self.send_header("Content-type", "text/xml")
            self.end_headers()
            self.wfile.write(bytes(return_file, "utf-8"))
        else:
            self.send_error(404, "Not Found", "Username requested does not exist")


myServer = HTTPServer((hostName, hostPort), MyServer)
print("Picture Server (beta) | Lei Yang i@yangl1996.com")
print(time.asctime(), "Picture Server Starts - %s:%s" % (hostName, hostPort))

try:
    myServer.serve_forever()
except KeyboardInterrupt:
    pass

myServer.server_close()
print(time.asctime(), "Picture Server Stops - %s:%s" % (hostName, hostPort))