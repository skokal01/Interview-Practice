# http://www.geeksforgeeks.org/design-a-stack-that-supports-getmin-in-o1-time-and-o1-extra-space/
from sys import maxint
class MyStack:
    def __init__(self):
        self.minimum = -maxint-1
        self.stack = []

    def push(self,val):
        if not self.stack:
            self.minimum = val
            self.stack.append(val)
        else:
            if val > self.minimum:
                self.stack.append(val)
            else:
                self.stack.append(2*val - self.minimum)
                self.minimum = val


    def pop(self):
        if self.stack:
            val = self.stack.pop()
            if val >= self.minimum:
                return val
            else:
                self.minimum = 2*self.minimum - val
                return self.minimum
        else:
            return None

if __name__ == "__main__":
    s = MyStack()
    print s.push(3), s.stack,s.minimum
    print s.push(5), s.stack,s.minimum
    print s.push(2), s.stack,s.minimum
    print s.push(1), s.stack,s.minimum
    print s.push(1), s.stack,s.minimum
    print s.push(-1), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
    print s.pop(), s.stack,s.minimum
