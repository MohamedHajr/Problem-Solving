function reversePrint(head) {
    if(head != null) {
        let stack = []
        while(head.next != null) {
            stack.push(head.data)
            head = head.next
        } 
        stack.push(head.data)

        while(stack.length > 0) {
            console.log(stack.pop())
        }
    }
}
