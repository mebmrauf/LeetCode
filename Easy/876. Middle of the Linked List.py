# 876. Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/

from typing import Optional
import math

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, count = head, 0
        while temp: count, temp = count + 1, temp.next

        count = math.floor(count/2)

        temp, c = head, 0
        while temp:
            if count == c: return temp
            c, temp = c + 1, temp.next