'''
https://discuss.leetcode.com/topic/15945/concise-1-queue-java-c-python
https://leetcode.com/problems/implement-stack-using-queues/#/discuss
'''
class MyStack:

    def __init__(self):
        self._queue = collections.deque()

    def push(self, x):
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)
