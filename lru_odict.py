# https:#discuss.leetcode.com/topic/14591/python-dict-double-linkedlist
from collections import OrderedDict
class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.lrucache = OrderedDict()

    def get(self, key):
        if key in self.lrucache:
            value = self.lrucache[key]
            del self.lrucache[key]
            self.lrucache[key] = value
            return value
        else:
            return -1

    def put(self, key, val):
        if key in self.lrucache:
            del self.lrucache[key]
        elif len(self.lrucache) >= self.capacity:
            k,v = self.lrucache.iteritems().next()
            del self.lrucache[k]

        self.lrucache[key] = val

if __name__ == "__main__":
    cache = LRUCache(2)

    cache.put(1,1)
    cache.put(2,2)
    print "After inserting 1,2 ", cache.lrucache
    print "Requesting 1 ",cache.get(1)
    print "After requesting 1 ", cache.lrucache
    cache.put(3,3)
    print "After inseting 3 ", cache.lrucache
    print "Requesting 2 ", cache.get(2)       # returns -1 (not found)
    cache.put(4, 4)    # evicts key 1
    print "After inserting 4 ", cache.lrucache
    print "Requesting 1 ", cache.get(1)       # returns -1 (not found)
    print "Requesting 3 ", cache.get(3)       # returns 3
    print "Requesting 4 ", cache.get(4)       # returns 4
    print "In the end ", cache.lrucache
