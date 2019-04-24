function sortedInsert(head, data) {
    const newNode = new Node(data)
    
    if(head == null || head.data >= data) {
        newNode.next = head
        newNode.prev = null
        return newNode
    }
    
    let prev = head
    let current = head.next

    while(current != null) {
        if(data < current.data) {
            prev.next = newNode
            newNode.prev = prev
            newNode.next = current
            return head
        }
        prev = prev.next
        current = current.next
    }
    
    if(prev.data > data){
            let first = prev.prev 
            first.next = newNode
            newNode.prev = first
            newNode.next = prev
    } else {
        prev.next = newNode
        newNode.prev = prev
        newNode.next = current
    }
    return head
