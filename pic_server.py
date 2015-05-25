__author__ = 'yangl1996'

import http.server
import socketserver

PORT = 8000
SERVER_ADDRESS = "128.199.244.33"

Handler = http.server.SimpleHTTPRequestHandler

httpd = socketserver.TCPServer((SERVER_ADDRESS, PORT), Handler)

print("Simple file server serving at ", SERVER_ADDRESS, ":", PORT)
httpd.serve_forever()