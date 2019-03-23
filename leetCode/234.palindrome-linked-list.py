#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (35.30%)
# Total Accepted:    235.3K
# Total Submissions: 664.7K
# Testcase Example:  '[1,2]'
#
# Given a singly linked list, determine if it is a palindrome.
# 
# Example 1:
# 
# 
# Input: 1->2
# Output: false
# 
# Example 2:
# 
# 
# Input: 1->2->2->1
# Output: true
# 
# Follow up:
# Could you do it in O(n) time and O(1) space?
# 
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow = head
        fast = head
        stack = []

        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next

        while slow:
            if slow.val != stack.pop():
                return False
            slow = slow.next
            
        return True

        

