from LinkedList import LinkedList


def getKthNode(head, k):
    if not head:
        return None, -1
    else:
        elem, counter = getKthNode(head.next, k)
        counter += 1
        if counter == k:
            elem = head
        return elem, counter


def kthElem(head, k):
    kthNode, _ = getKthNode(head, k)
    return kthNode.data


def findKthIterative(head, k):
    stack = []
    curr = head
    while curr:
        stack.append(curr)
        curr = curr.next
    counter = 0
    while counter != k:
        stack.pop()
        counter += 1
    return stack[-1].data

# iterative v2 2 pointers


def findKthElem(head, k):
    p1 = head
    p2 = head

    for k in range(k):
        if not p2:
            print('Incrrect LinkedList Out of bounds')
            return None
        p2 = p2.next

    while p2:
        p1 = p1.next
        p2 = p2.next
    return p1.data


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(findKthElem(ll.head, 1))

# v1
