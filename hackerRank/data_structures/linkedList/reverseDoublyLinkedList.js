function reverse(head) {
    let current = head
    let newHead = head
    while (current != null){
        const next = current.next
        current.next = current.prev
        current.prev = next
        newHead = current
        current = current.prev
    } 
    return newHead
}


