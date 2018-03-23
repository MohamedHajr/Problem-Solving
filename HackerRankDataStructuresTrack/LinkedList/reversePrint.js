function reversePrint(head) {
  if(head != null) {

    if(head == null || head.next == null) {
      console.log(head.data)
      return head
    }
    const leftOver = reversePrint(head.next)
    console.log(head.data)
    head.next.next = head
    head.next = null
    return leftOver
  }
}

const reverse = (head) => {
  if(head != null) {
    if(head == null || head.next == null) return head
    const leftOver = reverse(head.next)
    head.next.next = head
    head.next = null
    return leftOver
  }
}
