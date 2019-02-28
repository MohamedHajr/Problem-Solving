#
# @lc app=leetcode id=707 lang=python3
#
# [707] Design Linked List
#
# https://leetcode.com/problems/design-linked-list/description/
#
# algorithms
# Easy (22.87%)
# Total Accepted:    19.4K
# Total Submissions: 84.5K
# Testcase Example:  '["MyLinkedList","addAtHead","addAtTail","addAtIndex","get","deleteAtIndex","get"]\n[[],[1],[3],[1,2],[1],[1],[1]]'
#
# Design your implementation of the linked list. You can choose to use the
# singly linked list or the doubly linked list. A node in a singly linked list
# should have two attributes: val and next. val is the value of the current
# node, and next is a pointer/reference to the next node. If you want to use
# the doubly linked list, you will need one more attribute prev to indicate the
# previous node in the linked list. Assume all nodes in the linked list are
# 0-indexed.
#
# Implement these functions in your linked list class:
#
#
# get(index) : Get the value of the index-th node in the linked list. If the
# index is invalid, return -1.
# addAtHead(val) : Add a node of value val before the first element of the
# linked list. After the insertion, the new node will be the first node of the
# linked list.
# addAtTail(val) : Append a node of value val to the last element of the linked
# list.
# addAtIndex(index, val) : Add a node of value val before the index-th node in
# the linked list. If index equals to the length of linked list, the node will
# be appended to the end of linked list. If index is greater than the length,
# the node will not be inserted.
# deleteAtIndex(index) : Delete the index-th node in the linked list, if the
# index is valid.
#
#
# Example:
#
#
# MyLinkedList linkedList = new MyLinkedList();
# linkedList.addAtHead(1);
# linkedList.addAtTail(3);
# linkedList.addAtIndex(1, 2);  // linked list becomes 1->2->3
# linkedList.get(1);            // returns 2
# linkedList.deleteAtIndex(1);  // now the linked list is 1->3
# linkedList.get(1);            // returns 3
#
#
# Note:
#
#
# All values will be in the range of [1, 1000].
# The number of operations will be in the range of [1, 1000].
# Please do not use the built-in LinkedList library.
#
#


class Node:
    def __init__(self, val=None, pointer=None):
        self.data = val
        self.next = pointer


class MyLinkedList:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.size:
            return -1

        if self.head is None:
            return -1

        curr = self.head
        for _ in range(index):
            curr = curr.next
        return curr.data

    def addAtHead(self, val: int) -> None:
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        self.head = Node(val, self.head)
        self.size += 1

    def addAtTail(self, val: int) -> None:
        """
        Append a node of value val to the last element of the linked list.
        """
        if not self.head:
            self.addAtHead(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.size:
            return

        if index == 0:
            self.addAtHead(val)
        else:
            curr = self.head
            for _ in range(index - 1):
                curr = curr.next
            node = Node(val)
            node.next = curr.next
            curr.next = node

            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: void
        """
        if index < 0 or index >= self.size:
            return

        curr = self.head
        if index == 0:
            self.head = curr.next
        else:
            for _ in range(index - 1):
                curr = curr.next
            curr.next = curr.next.next

        self.size -= 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(0)
# obj.addAtHead(1)
# obj.addAtHead(2)
# obj.addAtHead(3)

# print(obj.get(0))
# print(obj.get(1))
# print(obj.get(2))
# print(obj.get(7))


# obj.deleteAtIndex(3)
# print(obj.get(4))
