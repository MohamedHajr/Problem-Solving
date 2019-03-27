# Enter your code here. Read input from STDIN. Print output to STDOUT
class stackNode:
    def __init__(self, data, maximum):
        self.data = data
        self.maximum = maximum

class Stack:
    def __init__(self):
        self.store = []
        self.maximum = 0

    def pop(self):
        elem = self.store.pop()
        if elem.data == self.maximum:
            if self.isEmpty():
                self.maximum = 0
            else:
                self.maximum = self.store[-1].maximum
        return


    def push(self, val):
        if val > self.maximum:
            self.maximum = val

        node = stackNode(val, self.maximum)
        self.store.append(node)
        return 

    def getMax(self):
        return self.maximum
    
    def isEmpty(self):
        return len(self.store) == 0

if __name__ == '__main__':
    N = int(input())
    queries = []
    for _ in range(N):
        queries.append(list(map(int, input().rstrip().split())))

    stack = Stack()

    for query in queries:
        kind = query[0]
        if kind == 1:
            stack.push(query[1])
        elif kind == 2:
            stack.pop()
        elif kind == 3:
            print(stack.getMax())



