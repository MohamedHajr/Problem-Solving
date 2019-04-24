#v1
class SetOfStacks:
    def __init__(self, capacity):
        self.stacks = []
        self.capacity = capacity

    def push(self, val):
        if len(self.stacks) == 0:
            print('New Incoming coming in...')
            self.add_new_stack(val)
            return True
        for stack in self.stacks:
            if len(stack) == self.capacity:
                continue
            stack.append(val)
            return True
        self.add_new_stack(val)
        return True

    def add_new_stack(self, val):
        self.stacks.append([val])

    def pop(self):
        if len(self.stacks) == 0:
            print('Da heck mate the stack is Empty! stop being retartd...')
            return False
        currStack = self.stacks[-1]
        poppedValue = currStack.pop()
        if len(currStack) == 0:
            self.stacks.pop()
        return poppedValue

    def popAtIndex(self, index):
        try:
            thatStack = self.stacks[index]
            popped = thatStack.pop()
            if len(thatStack) == 0:
                del self.stacks[index]
            return popped
        except:
            print('Da heck mate get a real index! stop being retartd...')
            return False

    def popAtIndexWithRollOver(self, index):
        try:
            curr = self.stacks[index]
            curr.pop()
            for stack in self.stacks[index + 1:]:
                poped = stack.pop()
                curr.append(poped)
                curr = stack
            if len(curr) == 0:
                del self.stacks[curr]
        except:
            print('Da heck mate get a real index! stop being retartd...')
            return False

#v2
class StackOfPlates:
    def __init__(self, limit):
        self.stacks = [[]]
        self.limit = limit
    
    def push(self, val):
        curr = self.stacks[-1]
        if len(curr) == self.limit:
            self.stacks.append([val])
        else:
            curr.append(val)

    def is_empty(self):
        return len(self.stacks[-1]) == 0

    def pop(self):
        if self.is_empty():
            return -1
        val = self.stacks[-1].pop()
        if len(self.stacks) > 1 and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return val            

    def pop_at(self, index):
        n = len(self.stacks)
        if index >= n:
            return -1 
        val = self.stacks[index].pop()
        if not (n-1) == index:
            for i in range(index, n-1):
                self.stacks[i].append(self.stacks[i+1].pop())

        if len(self.stacks[-1]) == 0:
            self.stacks.pop()
        return val

stacks = StackOfPlates(2)
print('popping at ...', stacks.pop())
stacks.push(1)
stacks.push(2)
stacks.push(3)
stacks.push(4)
stacks.push(5)
stacks.push(6)
print(stacks.stacks)
print('Popping...', stacks.pop_at(1))
print('Popping..', stacks.pop_at(2))
