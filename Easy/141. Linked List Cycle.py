# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        temp1, temp2 = head, head.next
        while temp1 != temp2:
            if not temp2 or not temp2.next:
                return False
            temp1, temp2 = temp1.next, temp2.next.next
        return True