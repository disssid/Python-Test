'''
Created on Jan 27, 2017

@author: sid
'''

from time import sleep

class process2:
    name =""
    def __init__(self,name):
        name = self.name
        
    def process2(self,q):
            for i in xrange(1,10):
                q.put(i)
                sleep(2)