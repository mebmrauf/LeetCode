# 921. Minimum Add to Make Parentheses Valid
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        openingParenthesis, closingParenthesis = 0, 0
        
        for parenthesis in s:
            if parenthesis == '(':
                openingParenthesis += 1
            else:
                if openingParenthesis > 0:
                    openingParenthesis -= 1
                else:
                    closingParenthesis += 1
        
        return openingParenthesis + closingParenthesis
    
# using stack
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for parenthesis in s:
            if stack and stack[-1] == '(' and parenthesis == ')':
                stack.pop()
            else:
                stack.append(parenthesis)
        return len(stack)