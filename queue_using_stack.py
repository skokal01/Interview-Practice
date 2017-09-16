class Queue(object):
    def __init__(self):
        self.inStack = []
        self.outStack = []

    def push(self,x):
        self.inStack.append(x)

    def pop(self):
        self.move()
        return self.outStack.pop()

    def peek(self):
        self.move()
        return self.outStack[-1]

    def empty(self):
        return (not self.inStack) and (not self.outStack)

    def move(self):
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

if __name__ == "__main__":
    q = Queue()
    q.push(1)
    q.push(2)
    print q.pop()
    print q.peek()
    print q.pop()
