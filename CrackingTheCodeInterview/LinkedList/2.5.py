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
    sm = headA.data + headB.data
    if sm >= 10:
        return (sm - 10 + rem), 1
    else:
        return sm + rem, 0


first = LinkedList()
first.append(7)
first.append(1)
first.append(6)
first.append(5)

second = LinkedList()
second.append(5)
second.append(9)
second.append(2)

result = sumLists(first.head, second.head)

while result:
    print(result.data)
    result = result.next
