from LinkedList import LinkedList


def reverse(head, linkedList=LinkedList()):
    if not head or not head.next:
        linkedList.append(head.data)
        return linkedList.head
    last = reverse(head.next)
    linkedList.append(head.data)
    return last


def isPalindrome_v1(head):
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
    return newHead.next, state


# print(isPalindromev2(ll.head, ll.head)[1])

# v3
def isPalindromev3(head):
    fast = head
    slow = head
    stack = []

    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next

    while slow:
        if slow.data != stack.pop():
            return False
        slow = slow.next
    return True



# v4
def isPalindromev4(linkedList):
    def isPalindrome(head, size):
        if not head or size <= 0:
            return True, head
        elif size == 1:
            return True, head.next

        status, node = isPalindrome(head.next, size - 2)

        if not status or not node:
            return status, node

        return head.data == node.data, node.next
    result, _ = isPalindrome(linkedList.head, linkedList.size)
    return result


print(isPalindromev4(ll))
