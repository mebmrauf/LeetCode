# 7. Reverse Integer
# https://leetcode.com/problems/reverse-integer

class Solution:
    def reverse(self, x: int) -> int:
        num = int(str(abs(x))[::-1])
        if x < 0:
            num *= -1 
        if math.pow(-2, 31) <= num <= math.pow(2, 31) - 1:
            return num
        return 0