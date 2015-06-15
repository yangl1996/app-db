from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import requests
import os

listenAddr = "128.199.82.190"
listenPort = 9999
db_file_path = "database.json"


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
            database_file = open(db_file_path, 'r')
            database = database_file.read()
            db = json.loads(database)
            database_file.close()
            if user_id not in db['user']:
                db['user'][user_id] = {}
                db['user'][user_id]["image_count"] = 0
                db['user'][user_id]["voice_count"] = 0
                db['user'][user_id]["image"] = []
                db['user'][user_id]["voice"] = []
            db['user'][user_id]['image_count'] += 1
            local_id = db['user'][user_id]['image_count']
            local_filename = str(local_id) + ".jpg"
            db['user'][user_id]['image'].append(local_filename)
            command = """
            cd FS
            mkdir """ + user_id + """
            cd """ + user_id + """
            wget -O """ + local_filename + " " + image_link + """
            """
            os.system(command)
            to_write = json.dumps(db)
            writer = open('database.json', 'w')
            writer.write(to_write)
            writer.close()

        elif data['MediaType'] == 'voice':
            user_id = data['Usr_Id']
            media_id = data['Media_Id']
            print("New voice from %s, URL is %s." % (user_id, media_id))
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