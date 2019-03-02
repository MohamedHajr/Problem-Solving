from LinkedList import LinkedList

def getKthNode(head, k, index):
    if not head:
        return None, -1
    else:
        curr, i = getKthNode(head.next, k,  index)
        i += 1
        if i == k:
            return head, i
        return curr, i

def kthElem(head, k):
    kthNode, _ = getKthNode(head, k, 0)
    return kthNode.data


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)

print(kthElem(ll.head ,0))

# v1
