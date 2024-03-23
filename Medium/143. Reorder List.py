# 143. Reorder List
# https://leetcode.com/problems/reorder-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        if not head:
            return
        
        mid = self.middleNode(head)
        l1, l2 = head, mid.next
        mid.next = None
        l2 = self.reverseList(l2)
        self.mergeList(l1, l2)
    
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def reverseList(self, head: ListNode) -> ListNode:
        prev, current = None, head
        while current:
            nextTemp = current.next
            current.next = prev
            prev = current
            current = nextTemp
        return prev

    def mergeList(self, l1: ListNode, l2: ListNode):
        while l1 and l2:
            l1Temp = l1.next
            l2Temp = l2.next

            l1.next = l2
            l1 = l1Temp

            l2.next = l1
            l2 = l2Temp
        """
        Do not return anything, modify head in-place instead.
        """