from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
import os

listenAddr = "128.199.82.190"
listenPort = 9999
db_file_path = "database.json"
last_image_id = -1


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
            db['count'] += 1
            global last_image_id
            last_image_id = db['count']
            local_filename = str(last_image_id) + ".jpg"
            local_fileURL = "http://" + listenAddr + ":8090" + "/FS/" + local_filename
            image_metadata = {'id': last_image_id, 'name': user_id, 'url': local_fileURL, 'text': "", 'audio': ""}
            db['image'].append(image_metadata)
            command = """
            cd FS
            wget -O {} {}""".format(local_filename, image_link)
            os.system(command)
            to_write = json.dumps(db)
            writer = open('database.json', 'w')
            writer.write(to_write)
            writer.close()

        elif data['MediaType'] == 'text':
            content = data['Content']
            if last_image_id != -1:
                database_file = open(db_file_path, 'r')
                database = database_file.read()
                db = json.loads(database)
                database_file.close()
                db['image'][last_image_id]['text'] = content
                to_write = json.dumps(db)
                writer = open('database.json', 'w')
                writer.write(to_write)
                writer.close()

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