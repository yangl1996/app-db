# Picture App server side script

*Note: The current version is only for test and demo purposes. I've NOT tested or built the program against possible safety threats.*

## Code Structure

### xml_server.py

Server program to serve XML files. It handles HTTP GET requests and responds XML file containing URLs of requested username if encounters no error.

By default this server serves at port 8080.

This is a well formatted request URL:

```
http://test.server.address:port/username
```

This is a example of returned XML file:

```
<resources>
  <string name="url_number">2</string>
  <string name="1">http://128.199.244.33:80/FS/test/test1.png</string>
  <string name="2">http://128.199.244.33:80/FS/test/test2.png</string>
</resources>
```

Under root node ```<resources>```, there is one ```<string>``` node specifying the number N of URLs following. Then follow N ```<string>``` nodes, each containing an URL.

There are two kinds of errors this program may throw:

* 500 Internal Error: there is no database found on server
* 404 Not Found: the requested username does not exist

### pic_server.py

This is a simple HTTP server serving EVERY file relative to its address. Be careful that I have NOT add any permission control for this server, so never place any private file with this server program.

By default it servers at port 80.

### init_database.py

This is an initializer for the database. It simply generates a JSON file as below:

```
{
  "test":
  [
    "http://128.199.244.33:80/FS/test/test1.png", "http://128.199.244.33:80/FS/test/test2.png"
  ]
}
```

By default you don't need to run this program. It is only used when the database is missing.

## Usage

By default, you just need to run these commands:

```
git clone https://github.com/yangl1996/app-db.git
cd app-db
```
Then change the server address in each file to correct value. And execute these comands:

```
python3 xml_server.py &
python3 pic_server.py &
```

For advanced usage, please contact me.

## Data Structure

* ./
  * FS/
    * username1/
    * username2/
    * ...
  * pic_server.py
  * init_database.py
  * xml_server.py
