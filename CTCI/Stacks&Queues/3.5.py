from Stack import Stack


def sortStack(unsortedStack):
    result = Stack()
    while not unsortedStack.isEmpty():
        tmp = unsortedStack.pop()
        while not result.isEmpty() and result.peek() > tmp:
            unsortedStack.push(result.pop())
        result.push(tmp)
    return result


unsortedStack = Stack([1, 2, 5, 6, 9, 3, 4])

result = sortStack(unsortedStack)
while not result.isEmpty():
    print('Elem -> ', result.pop())
