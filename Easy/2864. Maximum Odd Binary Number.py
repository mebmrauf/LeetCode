# 2864. Maximum Odd Binary Number
# https://leetcode.com/problems/maximum-odd-binary-number/description/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        if len(s) == 1:
            return s
        result, str0, str1 = '', '', ''
        for i in s:
            if i == '0':
                str0 += i
            else: str1 += i
        return str1[1:]+str0+'1'