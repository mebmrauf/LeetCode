# 19. Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp, count = head, 0
        # Calculate the length of the linked list
        while temp:
            count += 1
            temp = temp.next
        # Handle the case where the head needs to be removed
        if count == n:
            return head.next
        temp, c = head, 0
        # Traverse the list again to find the node before the one to be removed
        while temp:
            c += 1
            if c == count - n:
                temp.next = temp.next.next
                break
            temp = temp.next

        return head

# One pass Solution    
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next, first, second  = head, dummy, dummy

        # Move first pointer n+1 steps ahead
        for _ in range(n + 1):
            first = first.next
        # Move both pointers until the first pointer reaches the end
        while first is not None:
            first = first.next
            second = second.next
        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next