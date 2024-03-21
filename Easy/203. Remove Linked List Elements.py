# 203. Remove Linked List Elements
# https://leetcode.com/problems/remove-linked-list-elements/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Solution
# In-place
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head != None and head.val == val:
            head = head.next
        temp = head
        while temp:
            if temp.next != None and temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head

# Out-place    
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp, newHead = head, None
        while temp:
            if temp.val != val:
                if newHead is None:
                    newHead = ListNode(temp.val)
                    newTemp = newHead
                else:
                    node = ListNode(temp.val)
                    newTemp.next = node
                    newTemp = newTemp.next
            temp = temp.next
        return newHead
    
# Recursive Solution
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Base case: if head is None, return None
        if not head:
            return None
        
        # Recursively remove elements from the rest of the list
        head.next = self.removeElements(head.next, val)
        
        # Check if the current node's value is equal to val
        # If yes, return the next node, effectively removing the current node
        return head.next if head.val == val else head