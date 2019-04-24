/*
    Delete Node at a given position in a linked list
    head pointer input could be NULL as well for empty list
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.next = null;
    }
*/

// This is a "method-only" submission.
// You only need to complete this method.

function deleteNode(head, position) {
    if(head.next == null) return newNode
    
    let current = head
    let previous = head
    let i = 0
    while(i < position) {
        previous = current
        current = current.next
        i++
    }

    if(i == 0)  {
        head = head.next
        return head
    } else {
        previous.next = current.next
        return head
    } 
}


