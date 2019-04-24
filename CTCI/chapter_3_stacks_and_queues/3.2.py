#class Node:
#    def __init__(self, val, next=None):
#        self.val = val
#        self.next = next
#
##Todo Test dat shit
#class Stack:
#    def __init__(self):
#        self.size = 0
#        self.top = None
#        self.minHead = None
#
#    def push(self, val):
#        newNode = Node(val, self.top)
#        self.top = newNode
#        self.size += 1
#        self.minHead = self.add_to_min(self.minHead, val)
#
#    def getMin(self):
#        if self.isEmpty():
#            print("Oops!  The Stack is Empty.  fill it first Ahole...")
#            return -1
#        return self.minHead.val
#
#    def pop(self):
#        if self.size <= 0:
#            print("Oops!  The Stack is Empty.  fill it first Ahole...")
#            return -1
#        val = self.top.val
#        self.top = self.top.next
#        self.minHead = self.delete_from_min(self.minHead, val)
#        return val
#
#    def peek(self):
#        return self.top.val
#
#    def isEmpty(self):
#        return self.size == 0
#
#    def add_to_min(self, head, number):
#        newNode = Node(number)
#        if not head or number < head.val:
#            newNode.next = head
#            return newNode
#        curr = head
#        while curr.next:
#            if number < curr.next.val:
#                newNode.next = curr.next
#                break
#            curr = curr.next
#        curr.next = newNode
#        return head
#
#    def delete_from_min(self, head, number):
#        if number == head.val:
#            return head.next
#        curr = head
#        while curr.next:
#            if number == curr.next.val:
#                curr.next = curr.next.next
#                break
#            curr = curr.next
#        return head
#
#v2
class Node:
    def __init__(self, data, mini):
        self.data = data
        self.mini = mini
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.mini = 0xfffffff

    def push(self, val):
        if val < self.mini:
            self.mini = val
        new_node = Node(val, self.mini)
        new_node.next = self.top
        self.top = new_node

    def is_empty(self):
        return self.top is None

    def peek(self):
        if self.is_empty():
            return -1 
        return self.top.data

    def minimum(self):
        if self.is_empty():
            return -1 
        return self.top.mini

    def pull(self):
        if self.is_empty():
            return -1
        node = self.top
        self.top = self.top.next
        return node.data

stack = Stack()
stack.push(5)
stack.push(8)
stack.push(4)
stack.push(1)
stack.push(2)
print("mini should be 1 -> ", stack.minimum())
