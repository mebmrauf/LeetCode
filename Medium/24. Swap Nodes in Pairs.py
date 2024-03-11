# 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
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