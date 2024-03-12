# 1171. Remove Zero Sum Consecutive Nodes from Linked List
# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix, visited = 0, {}
        visited[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            visited[prefix] = head
            head = head.next
        head, prefix = dummy, 0
        while head:
            prefix += head.val
            head.next = visited[prefix].next
            head = head.next
        return dummy.next