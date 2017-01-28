'''
Created on Jan 27, 2017

@author: sid
'''

from multiprocessing import Process, Queue
from process2 import *
from Queue import Empty

if __name__ == '__main__':
    q = Queue()
    p = Process(target=function1, args=[q,])
    print "Starting function1 from process process2.py \n"
    p.start()
    p.is_alive()
    print "Control returned to process1 from process2.py \n"
    print "Waiting for data from Process2 \n"
    while 1:
        print "***************************************"
        try:
            data = q.get(timeout=3)
            print "data received from process2 -",data
            print "***************************************\n"
        except Empty:
            print "Queue empty terminating process1"
            break
        
    p.terminate()
    