from Stack import Node


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.size = 0

    def add(self, val):
        newNode = Node(val)
        self.size += 1
        if self.last:
            self.last.next = newNode
        self.last = newNode
        if not self.first:
            self.first = self.last

    def remove(self):
        if self.size == 0:
            print("Oops!  The Queue is Empty.  fill it first Ahole...")
            return -1
        self.size -= 1
        first = self.first.val
        self.first = self.first.next
        if not self.first:
            self.last = None
        return first

    def peek(self):
        if self.size == 0:
            print("Oops!  The Queue is Empty.  fill it first Ahole...")
            return -1
        return self.first.val

    def isEmpty(self):
        return self.size == 0


queue = Queue()
queue.add(5)
queue.add(6)

popped1 = queue.remove()
popped2 = queue.remove()
popped3 = queue.remove()

print('suppose to be 5 -> ', popped1)
print('suppose to be 6 -> ', popped2)
print('suppose to be -1 -> ', popped3)
