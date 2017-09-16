'''
# Write a program to produce a list of 3 closest addresses to the city center
# based on the supplied distance from the city center per address for a given
# set of addresses

i/p: (address,d), k -- number of closest addresses
o/p: List[(address,distance)]

'''
# Code for implementing custom comparators,
# this is not currently used in the solution
# wrote it for reference purposes
class Address(object):
    def __init__(self,distance,address):
        self.distance = distance
        self.address = address

    def __cmp__(self,other):
        return cmp(self.distance,other.distance)

import heapq
def getKClosestAddresses(addresses,k):
    '''
    :addresses list of pairs with address and distance
    '''
    if k < 0:
        return []

    if not addresses:
        return []

    h = []
    for i in addresses:
        #a,d = i.address,i.distance
        heapq.heappush(h,i)

    ret = []
    for i in xrange(k):
        a = heapq.heappop(h)
        ret.append((a.address,a.distance))

    return ret

if __name__ == "__main__":
    addresses = [Address(5,"FRE"),Address(10,"SFO"),Address(4,"OAK"),Address(20,"SJC"),Address(100,"LAX"),Address(2,"MIL")]
    print getKClosestAddresses(addresses,3)
