# https://discuss.leetcode.com/topic/14591/python-dict-double-linkedlist
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class data:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)

        # Initialized a Double List and point head and tail to
        # each other
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        if key in self.data:
            node = self.data[key]
            # Remove and add it to the recent position
            self._remove(node)
            self._add(node)
            return node.val
        else:
            return -1

    def put(self, key, val):
        if key in self.data:
            # Key is present, remove it and add it to recent position
            node = self.data[key]
            self._remove(node)

        node = Node(key, val)
        self._add(node)
        self.data[key] = node

        # If capacity is reached remove the lru one
        if len(self.data) > self.capacity:
            tmp = self.head.next
            self._remove(tmp)
            del self.data[tmp.key]

    def _add(self, node):
        p = self.tail.prev
        p.next = node
        node.prev = p
        node.next = self.tail

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

if __name__ == "__main__":
        cache = data(2)

        cache.put(1,1)
        cache.put(2,2)
        print "After inserting 1,2 ", cache.data
        print "Requesting 1 ",cache.get(1)
        print "After requesting 1 ", cache.data
        cache.put(3,3)
        print "After inseting 3 ", cache.data
        print "Requesting 2 ", cache.get(2)       # returns -1 (not found)
        cache.put(4, 4)    # evicts key 1
        print "After inserting 4 ", cache.data
        print "Requesting 1 ", cache.get(1)       # returns -1 (not found)
        print "Requesting 3 ", cache.get(3)       # returns 3
        print "Requesting 4 ", cache.get(4)       # returns 4
        print "In the end ", cache.data
