# 150. Evaluate Reverse Polish Notation
# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                stack.append(int(token))
            else:
                if token == '+':
                    stack[-2] += stack[-1]
                elif token == '-':
                    stack[-2] -= stack[-1]
                elif token == '*':
                    stack[-2] *= stack[-1]
                elif token == '/':
                    stack[-2] = int(stack[-2]/stack[-1])
                stack.pop()
        return stack[0]