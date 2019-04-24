function findMergeNode(headA, headB) {
    let currentA = headA.next
    let currentB = headB.next
    
    while(currentA != currentB) {
        //if we reached the end of a list start at the beggining of the other one
        currentA.next == null ? currentA = headB
        : currentA = currentA.next
        currentB.next == null ? currentB = headA
        : currentB = currentB.next
    }
    return currentA.data
}
