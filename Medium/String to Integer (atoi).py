# 8. String to Integer (atoi)
# https://leetcode.com/problems/string-to-integer-atoi

class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if not s:
            return 0

        sign = 1
        if s[0] in ('+', '-'):
            sign = -1 if s[0] == '-' else 1
            s = s[1:]

        result = 0
        for char in s:
            if char.isdigit():
                result = result * 10 + int(char)
            else:
                break

        result *= sign
        return max(min(result, 2**31 - 1), -2**31)