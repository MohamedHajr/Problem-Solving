from LinkedList import Node, LinkedList

# v1


def sumLists(headA, headB):
    resultList = None
    reminder = 0

    while headA and headB:
        final, rem = getNodeResult(headA, headB, reminder)
        reminder = rem
        newNode = Node(final)
        if not resultList:
            resultList = newNode
        else:
            newNode.next = resultList
            resultList = newNode
        headA = headA.next
        headB = headB.next

    if headA:
        while headA:
            newNode = Node(headA.data, resultList)
            resultList = newNode
            headA = headA.next

    if headB:
        while headB:
            newNode = Node(headB.data, resultList)
            resultList = newNode
            headB = headB.next
    return resultList


def getNodeResult(headA, headB, rem):
    sm = headA.data + headB.data + rem
    if sm >= 10:
        return (sm - 10), 1
    else:
        return sm, 0


first = LinkedList()
first.append(7)
first.append(1)
first.append(6)

second = LinkedList()
second.append(5)
second.append(9)
second.append(2)

result = sumLists(first.head, second.head)

# while result:
#     print(result.data)
#     result = result.next


def sumListsRecursive(headA, headB):

    def calculateSumition(a, b, reminder):
        total = a.data + b.data + reminder
        rem = 0
        if total >= 10:
            rem = total - 10
        return total, rem

    def calc(headA, headB, reminder, result):
        if headA and headB:
            total, rem = calculateSumition(headA, headB, reminder)
            newNode = Node(total)
            if not result:
                result = newNode
            else:
                result.next = newNode
            calc(headA.next, headB.next, rem, result.next)
        elif headA:
            newNode = Node(headA.val)
            calc(headA.next, headB, rem, result.next)
        elif headB:
            newNode = Node(headB.val)
            result.next = newNode
            calc(headA, headB.next, rem, result.next)

        return result

    return calc(headA, headB, 0, None)


result = sumListsRecursive(first.head, second.head)
while result:
    print(result.data)
    result = result.next
