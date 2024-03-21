# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Solution       
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            # Swap nodes
            firstNode.next = secondNode.next
            secondNode.next = firstNode
            prev.next = secondNode

            # Move to the next pair
            prev = firstNode
            head = firstNode.next

        return dummy.next

# Recursive Solution
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if the list is empty or has only one node, no need to swap, return head
        if not head or not head.next:
            return head
        
        # Store the next node after head
        next = head.next
        
        # Swap the first two nodes and recurse for the rest of the list
        head.next = self.swapPairs(next.next)
        next.next = head
        
        # Return the new head (which is the second node after swapping)
        return next