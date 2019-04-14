class MyQueue:
    def __init__(self):
        self.readStack = []
        self.pushStack = []

    def add(self, val):
        self.pushStack.append(val)

    def shiftStacks(self):
        self.readStack = self.pushStack[::-1]

    def remove(self):
        if len(self.readStack) == 0:
            self.shiftStacks()
        return self.readStack.pop()

myQueue = MyQueue()
myQueue.add(5)
myQueue.add(6)
myQueue.add(7)

print('Popped value should be -> 5', myQueue.remove())
print('Popped value should be -> 6', myQueue.remove())
print('Popped value should be -> 7', myQueue.remove())