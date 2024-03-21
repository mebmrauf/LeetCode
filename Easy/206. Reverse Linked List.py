# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Recursive Solution        
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        reversedHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return reversedHead
    
# Iterative Solution
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        current = head
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next
        return prev