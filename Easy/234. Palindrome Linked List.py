# 234. Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # Helper function to reverse a linked list
        def reverseLinkedList(node):
            prev = None
            current = node
            while current:
                nextNode = current.next
                current.next = prev
                prev = current
                current = nextNode
            return prev
        
        # Find the middle of the linked list using slow and fast pointers
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Reverse the second half of the linked list
        secondHalf = reverseLinkedList(slow)
        
        # Compare the first half with the reversed second half
        while secondHalf:
            if head.val != secondHalf.val:
                return False
            head = head.next
            secondHalf = secondHalf.next
        return True