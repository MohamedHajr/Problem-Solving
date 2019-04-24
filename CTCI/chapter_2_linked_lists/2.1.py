from LinkedList import LinkedList

#V1
def deleteDuplicates(head):
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


def removeDup(head):
    curr = head
    while curr:
        runner = curr
        while runner.next:
            if runner.next.data == curr.data:
                runner.next = runner.next.next
            else:
                runner = runner.next
        curr = curr.next

#idk what is this, this is the kind of code you regret writing
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
    



# that only would works for characters
def removeDuplicates(head):
    bitVector = 0
    if not head:
        return head
    bitVector |=  1 << ord(head.data) 
    curr = head
    while curr.next:
        binary = 1 << ord(curr.next.data) 
        if bitVector & binary > 0:
            curr.next = curr.next.next
        bitVector |= binary
    return head

ll = LinkedList()
ll.append(1)
ll.append('b')
ll.append('c')
ll.append('d')
ll.append('x')
