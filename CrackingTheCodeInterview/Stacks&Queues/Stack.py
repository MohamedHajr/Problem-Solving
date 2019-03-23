class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Stack:
    def __init__(self):
        self.size = 0
        self.top = None

    def push(self, val):
        newNode = Node(val, self.top)
        self.top = newNode
        self.size += 1

    def delete(self):
        if self.size <= 0:
            print("Oops!  The Stack is Empty.  fill it first Ahole...")
            return -1
        self.top = self.top.next
        self.size -= 1

    def pop(self):
        if self.size <= 0:
            print("Oops!  The Stack is Empty.  fill it first Ahole...")
            return -1
        val = self.top.val
        self.delete()
        return val

    def peek(self):
        return self.top.val
    def isEmpty(self):
        return self.size == 0


stack = Stack()
stack.push(5)
stack.push(6)
popped1 = stack.pop()
popped2 = stack.pop()
popped3 = stack.pop()

print('suppose to be 6 -> ', popped1)
print('suppose to be 5 -> ', popped2)
print('suppose to be -1 -> ', popped3)
