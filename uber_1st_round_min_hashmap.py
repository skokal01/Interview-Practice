## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.
## MinHashMap, MinDict
## hashmap, put(K,V), get(K), minValue(), remove(K)
import heapq
class MinHashMap(object):
    def __init__(self):
        self.hashmap = []

    def put(self,k,v):
        heapq.heappush(self.hashmap, (k,v))

    def get(self,k):
        for i in self.hashmap:
            if i[0] == k:
                return i[1]

        return -1

    def minValue(self):
        minimum = heapq.nsmallest(1,self.hashmap)
        return minimum[0][0]

    def remove(self,k):
        for index,val in enumerate(self.hashmap):
            if val[0] == k:
                self.hashmap.pop(index)
                heapq.heapify(self.hashmap)
                return
if __name__ == "__main__":
    mh = MinHashMap()
    mh.put(1,1)
    print mh.minValue() # 1
    mh.put(2,2)
    print mh.minValue() # 1
    print mh.get(1)     # 1
    mh.remove(1)
    print mh.minValue() # 2


    '''

Stdin
Stdout
Run Code (Alt + R) Open Chat
