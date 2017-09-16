from threading import Lock
import time

class myQueue(object):
    def __init__(self,maxSize):
        self.q = []
        self.len = maxSize
        self.lock = Lock()

    def get(self):
        consumed = False
        while not consumed:
            self.lock.acquire()
            if not self.isEmpty():
                item = self.q.pop(0)
                consumed = True
            self.lock.release()
            time.sleep(1000)

        return item

    def add(self,item):
        produced = False
        while not produced:
            self.lock.acquire()
            if self.len != self.getlen():
                self.q.append(item)
                produced = True
            self.lock.release()
            time.sleep(1000)

    def isEmpty(self):
        return len(self.q) == 0

    def getLen(self):
        return len(self.q)
