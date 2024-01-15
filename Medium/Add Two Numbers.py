# 2. Add Two Numbers
# https://leetcode.com/problems/add-two-numbers

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