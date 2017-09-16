from threading import Lock
class MyLock(object):
    def __init__(self):
        self.lock = Lock()

    def __enter__(self):
        self.lock.acquire()
        print "Acquired the lock"

    def __exit__(self,exception_type, exception_value, traceback):
        self.lock.release()
        print "Released the lock"

if __name__ == "__main__":
    with MyLock():
        print "In critical section"
