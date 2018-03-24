/*
    Remove all duplicate elements from a sorted Linked List
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.next = null;
    }
*/

// This is a "method-only" submission.
// You only need to complete this method.

function removeDuplicates(head) {
    if(head == null) return null
    if(head.next == null) return head
    return findAndRemoveDuplicates(head, head.next, head)
}

const findAndRemoveDuplicates = (prev, current, head) => {
    if(current == null) return head
    if(prev.data == current.data) {
        prev.next = current.next
        findAndRemoveDuplicates(prev, prev.next, head)
    } else findAndRemoveDuplicates(current, current.next, head)
}


