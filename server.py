__author__ = 'yangl1996'
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer

PORT_NUMBER = 8080



class MyHandler(BaseHTTPRequestHandler):

    # Handler for the GET requests
    def do_GET(self):
        print('Get request received')
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        # Send the html message
        self.wfile.write("Hello World !")
        return

try:
    # Create a web server and define the handler to manage the
    # incoming request
    server = HTTPServer(('', PORT_NUMBER), MyHandler)
    print('Started server on port ', PORT_NUMBER)

    # Wait forever for incoming http requests
    server.serve_forever()

finally:
    print("Error encountered, shutting down")