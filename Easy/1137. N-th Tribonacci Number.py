# 1137. N-th Tribonacci Number
# https://leetcode.com/problems/n-th-tribonacci-number/

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        
        first, second, third = 0, 1, 1
        
        for i in range(3, n + 1):
            fourth = first + second + third
            first, second, third = second, third, fourth
        
        return third