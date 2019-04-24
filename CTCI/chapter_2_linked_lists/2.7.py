from LinkedList import LinkedList, Node
# v1


def isIntersected(headA, headB):
    currA = headA
    currB = headB
    while currA or currB:
        if currA == currB:
            return True
        if not currA:
            currA = headB
        else:
            currA = currA.next

        if not currB:
            currB = headA
        else:
            currB = currB.next
    return False

intersection = Node('g')

llA = LinkedList()
llA.append('a')
llA.append('b')
llA.append('c')
llA.append('d')
llA.tail.next = intersection

llB = LinkedList()
llB.append('z')
llB.append('x')
llB.tail.next = intersection

print(isIntersected(llA.head, llB.head))
