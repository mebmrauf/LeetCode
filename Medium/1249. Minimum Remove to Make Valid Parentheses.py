# 1249. Minimum Remove to Make Valid Parentheses
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        result = []
        stack = []
        for char in s:
            if char not in '()': result.append(char)
            elif char == ')':
                if stack:
                    stack.pop()
                    result.append(')')
            else:
                stack.append(len(result))
                result.append('(')
        stack = set(stack)
        result = [x for index, x in enumerate(result) if index not in stack]
        return ''.join(result)