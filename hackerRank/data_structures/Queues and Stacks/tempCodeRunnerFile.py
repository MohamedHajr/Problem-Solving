class Stack:
#     def __init__(self):
#         self.store = []
#         self.maximum = LinkedList()

#     def pop(self):
#         elem =  self.store.pop()
#         self.maximum.remove(elem)
#         return elem


#     def push(self, val):
#         self.store.append(val)
#         self.maximum.add(val)
#         return 

#     def getMax(self):
#         return self.maximum.peek()
    
#     def isEmpty(self):
#         return len(self.store) == 0

# if __name__ == '__main__':
#     N = int(input())
#     queries = []
#     for _ in range(N):
#         queries.append(list(map(int, input().rstrip().split())))

#     stack = Stack()

#     for query in queries:
#         kind = query[0]
#         if kind == 1:
#             stack.push(query[1])
#         elif kind == 2:
#             stack.pop()
#         elif kind == 3:
#             print(stack.getMax())

