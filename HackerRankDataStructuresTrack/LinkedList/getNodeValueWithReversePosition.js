function getNodeValue( head, position) {

  if(head == null) return null

  const reversedHead = reverse(head)    
  if(position == 0) return reversedHead.data
  let i = 0
  let current = reversedHead

  while (i < position) {
    current = current.next
    i++
  }
  return current.data
}

const reverse = (head) => {
    if(head == null) return null 
    else {
      if(head == null || head.next == null) return head
        const leftOver = reverse(head.next)
        head.next.next = head
        head.next = null
        return leftOver
    }
}

