# 402. Remove K Digits
# https://leetcode.com/problems/remove-k-digits/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        
        for digit in num:
            while k and stack and stack[-1] > digit:
                stack.pop()
                k -= 1
        
            stack.append(digit)
        
        result = stack[:-k] if k else stack
        
        return "".join(result).lstrip('0') or "0"