from LinkedList import LinkedList

# v1


def deleteMid(head):
    head.data = head.next.data
    if not head.next.next:
        head.next = None
    else:
        deleteMid(head.next)

# v2


def deleteMidv2(head):
    if not head or not head.next:
        return None
    nex = head.next
    head.data = nex.data
    head.next = nex.next
    return


ll = LinkedList()
ll.append(1)
ll.append(5)
ll.append(9)
ll.append(12)

deleteMid(ll.head.next.next)
for n in ll:
    print(str(n))
