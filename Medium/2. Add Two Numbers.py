# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Iterative Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1, num2 = '', ''
        while l1:
            num1 += str(l1.val)
            l1 = l1.next
        while l2:
            num2 += str(l2.val)
            l2 = l2.next
        num1, num2 = int(num1[::-1]), int(num2[::-1])
        num = (str(num1+num2))[::-1]
        head = ListNode(num[0])
        temp = head
        for i in num[1:]:
            temp.next = ListNode(i)
            temp = temp.next
        return head

# Recursive Solution
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], carry=0) -> Optional[ListNode]:
        # Base case: if both lists are None and there's no carry, return None
        if not l1 and not l2 and carry == 0:
            return None
        
        # Calculate the sum of current digits and the carry from previous operation
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        
        # Calculate the carry for the next operation
        carry = total // 10
        
        # Create a new node with the value of the sum modulo 10
        node = ListNode(total % 10)
        
        # Recursively call the function for the next nodes in both lists
        l1Next = l1.next if l1 else None
        l2Next = l2.next if l2 else None
        node.next = self.addTwoNumbers(l1Next, l2Next, carry)
        
        return node