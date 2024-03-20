# 1669. Merge In Between Linked Lists
# https://leetcode.com/problems/merge-in-between-linked-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the ath node and the node after the bth node in list1
        beforeA, afterB, current, count = None, None, list1, 0

        while current:
            if count == a - 1: beforeA = current
            if count == b + 1: afterB = current
            current, count = current.next, count + 1
        
        # Connect the ath node to the head of list2
        beforeA.next = list2
        
        # Find the end of list2
        endList2 = list2
        while endList2.next: endList2 = endList2.next
        
        # Connect the end of list2 to the node after the bth node
        endList2.next = afterB
        
        return list1