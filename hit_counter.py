'''
https://nuttynanaus.wordpress.com/2014/03/09/software-engineer-interview-questions/
https://discuss.leetcode.com/topic/48788/48ms-python-concise-solution
'''
from collections import deque

class HitCounter(object):
    def __init__(self,minutes):
        self.counter = 0;
        self.hits = deque(maxlen=minutes*60)

    def hit(self,timestamp):
        if not self.hits or self.hits[-1][0] != timestamp:
            self.hits.append([timestamp,1])
        else:
            self.hits[-1][1] += 1

        self.counter += 1

    def getHits(self,timestamp):
        while self.hits and self.hits[0][0] <= timestamp:
            self.counter -= self.hits.popleft()[1]

        return self.counter
