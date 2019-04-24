/*
    Merge two sorted lists A and B as one Linked List and return the head of merged list
    Node is defined as
    var Node = function(data) {
        this.data = data;
        this.next = null;
    }
*/

// This is a "method-only" submission.
// You only need to complete this method.
function mergeLinkedLists( headA, headB) {
  if(headA == null && headB == null) return null
  else if (headB == null) return headA
  else if (headA == null) return headB

  if(headA.data < headB.data) {
    headA.next = mergeLinkedLists(headA.next, headB)
  } else {
    let temp = headB
    headB = headB.next
    temp.next = headA
    headA = temp
    headA.next = mergeLinkedLists(headA.next, headB)
  }
  return headA
}
