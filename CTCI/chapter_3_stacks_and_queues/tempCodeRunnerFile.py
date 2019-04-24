    while not unsortedStack.isEmpty():
        tmp = unsortedStack.pop()
        while not result.isEmpty() and tmp > result.peek():
            unsortedStack.push(result.pop())
        result.push(tmp)