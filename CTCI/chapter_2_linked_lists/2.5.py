from LinkedList import Node, LinkedList

# v1
def sumLists(headA, headB):
    final = []
    reminder = 0

    while headA and headB:
        total = headA.data + headB.data + reminder
        if total > 10:
            reminder = 1
            final.append(total - 10)
        else:
            reminder = 0
            final.append(total)
        headA = headA.next
        headB = headB.next

    while headA:
        final.append(headA.data)
        headA = headA.next

    while headB:
        final.append(headB.data)
        headB = headB.next
    return int(''.join(str(x) for x in final[::-1]))

first = LinkedList()

first.append(7)
first.append(1)
first.append(6)

second = LinkedList()
second.append(5)
second.append(9)
second.append(2)

result = sumLists(first.head, second.head)
print(result)

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
