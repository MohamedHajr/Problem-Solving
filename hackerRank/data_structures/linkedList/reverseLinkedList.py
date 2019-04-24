class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    @property
    def data(self):
        return self.data
    
    @property
    def next(self):
        return self.next

    def set_next(self, next):
        self.next = next
