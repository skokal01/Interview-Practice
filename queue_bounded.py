from threading import Thread,Condition
import logging
import time
import random

logging.basicConfig(level=logging.DEBUG,
                    format='[%(levelname)s] (%(threadName)-10s) %(message)s',
                    )

class myQueue(object):
    def __init__(self,size):
        self.q = []
        self.len = size
        self.cv = Condition()

    def get(self):
        item = 0
        with self.cv:
            while self.isEmpty():
                self.cv.wait()
            item = self.q.pop(0)
            logging.debug('Consumed ' + str(item) + " : " + str(self.q))
        return item

    def put(self,item):
        with self.cv:
            if not self.isFull():
                self.q.append(item)
                logging.debug('Produced ' + str(item) + " : " + str(self.q))
                self.cv.notify()

    def isEmpty(self):
        return len(self.q) == 0

    def isFull(self):
        return len(self.q) == self.len

    def getLen(self):
        return len(self.q)

def producer(myQ):
    count = 11
    while count:
        item = random.randint(1,100)
        myQ.put(item)
        time.sleep(random.randint(1,2))
        count -= 1

def consumer(myQ):
    count = 10
    while count:
        item = myQ.get()
        time.sleep(random.randint(1,5))
        count -= 1

def test2(myQ):
    print myQ.get()

def testThread(myQ):
    myQ.put(1)

if __name__ == "__main__":
    myQ = myQueue(4)

    # t2 = Thread(target=test2, args = (myQ,))
    # t = Thread(target=testThread, args = (myQ,))
    # t2.start()
    # t.start()
    # t.join()
    # t2.join()
    p = Thread(target=producer, args = (myQ,))
    c = Thread(target=consumer, args = (myQ,))

    p.start()
    c.start()

    p.join()
    c.join()
