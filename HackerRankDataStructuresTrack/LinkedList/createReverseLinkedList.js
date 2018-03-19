function reverseLinkedList(head) {
    if(head == null) return null 
    else {
        let stack = []
        while(head.next != null) {
            stack.push(head.data)
            head = head.next
        } 
        stack.push(head.data)
        
        //Creatring New LinkedList
        const newHeadNode = new Node(stack.pop())
        let lastNode = newHeadNode
        
        while(stack.length > 0) {
            const newNode = new Node(stack.pop())
            lastNode.next = newNode
            lastNode = newNode
        }
        return newHeadNode
    }
}
