from LinkedList import LinkedList


def reverse(head, linkedList=LinkedList()):
    if not head or not head.next:
        linkedList.append(head.data)
        return linkedList.head
    last = reverse(head.next)
    linkedList.append(head.data)
    return last


def isPalindrome(head):
    rev = reverse(head)

    while head:
        if head.data == rev.data:

            head = head.next
            rev = rev.next
        else:
            return False
    return True


ll = LinkedList()
ll.append('b')
ll.append('a')
ll.append('a')
ll.append('b')
# v2


def isPalindromev2(head, tail):
    if not tail:
        return head, True

    newHead, state = isPalindromev2(head, tail.next)

    if tail.data != newHead.data:
        state = False
    print('tail ->', tail.data)
    print('head ->', newHead.data)
    print('********')

    newHead = head.next
    return newHead, state


print(isPalindromev2(ll.head, ll.head))
