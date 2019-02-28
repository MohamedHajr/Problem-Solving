class Node:
    def __init__(self, val=None, pointer=None):
        self.data = val
        self.next = pointer


class LinkedList:
    def __init__(self):
        self.head = None
        self.current = None

    def append(self, val):
        newNode = Node(val)
        if self.head == None:
            self.head = newNode
            self.current = newNode
            return

        n = self.head
        while n.next != None:
            n = n.next
        n.next = newNode
        return self.head

    def delete(self, val):
        if self.head.data == val:
            self.head = self.head.next
        current = self.head
        while current.next:
            if current.next.data == val:
                current.next = current.next.next
                return True
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self.current != None:
            n = self.current
            self.current = n.next
            return n.data
        else:
            self.current = self.head
            raise StopIteration