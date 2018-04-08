function reverseLinkedList(head) {
  if(head == null) return null 
  else {
      if(head == null || head.next == null) return head
      const leftOver = reverseLinkedList(head.next)
      head.next.next = head
      head.next = null
      return leftOver
  }
}
