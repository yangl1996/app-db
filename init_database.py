__author__ = 'yangl1996'
import json
hostName = "128.199.244.33"
hostPort = 8090
test_string1 = "http://" + hostName + ":" + str(hostPort) + "/FS/test/test1.png"
test_string2 = "http://" + hostName + ":" + str(hostPort) + "/FS/test/test2.png"
test_database_data = {"test": [test_string1, test_string2]}
to_write = json.dumps(test_database_data)
writer = open('database.json', 'w')
writer.write(to_write)
writer.close()