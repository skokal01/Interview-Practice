## This is the text editor interface.
## Anything you type or change here will be seen by the other person in real time.
##
## MinStack, stack, push, pop, peek, min
## push 5, min -> 5
## push 1, min -> 1
## pop -> 1, min -> 5
##
## push (x) if x > minEle stack.append(x)
## stack.append(2*x-minEle)
## x = pop () if x > minEle return x
## else : return(2*minEle -x)

from sys import maxint
class MinStack(object):
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
                self.stack.append(2*val-self.minimum)
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
            raise Exception("Stack Empty")

    def getMinimum(self):
        return self.minimum

    def peek(self):
        if self.stack:
            val = self.stack[-1]
            if val >= self.minimum:
                return val
            else:
                return 2*self.minimum-val
        else:
            raise ValueError("Stack Empty")

if __name__ == "__main__":
    s = MinStack()
    s.push(5)
    print s.getMinimum() # 5
    s.push(1)
    print s.getMinimum() # 1
    s.pop()
    print s.getMinimum() # 5
    print s.peek()  # 5
    print s.pop()  # 5
    print s.pop() # Exception
