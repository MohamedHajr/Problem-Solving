from LinkedList import LinkedList

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(1)

def deleteDuplicates(head=ll.head):
    index = head
    while index.next:
        prev = index
        curr = index.next
        while curr:
            if index.data == curr.data:
                print('deleting ', index.data)
                prev.next = curr.next
                curr = curr.next
            else:
                prev = prev.next
                curr = curr.next
        index = index.next

def iterateOver(head, k):
    last = None
    if head.next != None:
       last = iterateOver(head.next, k)
    else:
        if last == k:
            return head.data 
        return 0
    last += 1
    if last == k:
        return head.data
    
deleteDuplicates()
for n in ll:
    print('number -> ', n)
