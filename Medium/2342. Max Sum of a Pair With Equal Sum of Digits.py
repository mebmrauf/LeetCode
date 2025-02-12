# 2342. Max Sum of a Pair With Equal Sum of Digits
# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/

from collections import defaultdict

class Solution:
    def maximumSum(self, nums):
        digitSum = defaultdict(int)
        maxSum = -1

        for num in nums:
            dSum = sum(int(digit) for digit in str(num))
            if dSum in digitSum:
                maxSum = max(maxSum, num + digitSum[dSum])
                digitSum[dSum] = max(num, digitSum[dSum])
            else:
                digitSum[dSum] = num

        return maxSum