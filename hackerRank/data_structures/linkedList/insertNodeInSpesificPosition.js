/*
  Insert Node at a given position in a linked list 
  head can be NULL 
  First element in the linked list is at position 0
  Node is defined as
  var Node = function(data) {
    this.data = data;
    this.next = null;
  }
*/

// This is a "method-only" submission.
// You only need to complete this method.

function insert(head, data, position) {
    const newNode = new Node(data)
    if(head == null) return newNode
    
    let current = head
    let previous = head
    let i = 0
    while(i < position) {
        previous = current
        current = current.next
        i++
    }

    if(i == 0)  {
        previous = newNode
        previous.next = current
        return previous
    } else {
        previous.next = newNode
        newNode.next = current
        return head
    } 
}
