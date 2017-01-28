'''
Created on Jan 27, 2017

@author: sid
'''
from time import sleep

def function1(q):
    for i in xrange(1,5):
        q.put(i)
        sleep(2)