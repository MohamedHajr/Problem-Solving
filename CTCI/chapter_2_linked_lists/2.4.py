from LinkedList import LinkedList

#v1 
def splitAround(head, x):
    newL = LinkedList()
    curr = head
    while curr:
        if curr.data >= x:
            newL.append(curr.data)
        else:
            newL.appendFromHead(curr.data)
        curr = curr.next
    return newL.head


ll = LinkedList()
ll.append(3)
ll.append(5)
ll.append(8)
ll.append(5)
ll.append(10)
ll.append(2)
ll.append(1)

newHead = splitAround(ll.head, 5)
curr = newHead
while curr:
    print('Number ->', curr.data)
    curr = curr.next
