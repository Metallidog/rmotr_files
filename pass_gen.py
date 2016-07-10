import string
from random import choice

class SimplePasswordGenerator(object):
    def __init__(self, available_chars=None, length=8):
        if available_chars:
            self.chars = available_chars
        else:
            self.chars = list(string.ascii_letters + string.digits + string.punctuation)
        self.length = length
        
    def __iter__(self):
        return self
        
    def build(self):
    	return ''.join(choice(self.chars) for _ in range(self.length)) 

    def next(self):  # use __next__ in Python 3.x
        return  self.build()
        
    def __next__(self):
        return self.build()    
        
p = SimplePasswordGenerator()

print (next(p))
print (next(p))
print (next(p))
