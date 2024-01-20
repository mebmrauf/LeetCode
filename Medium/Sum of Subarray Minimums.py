# 907. Sum of Subarray Minimums
# https://leetcode.com/problems/sum-of-subarray-minimums/

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        subArrays, miniSum, modulo = [], 0, 10**9 + 7

        for i in range(len(arr)):
            while subArrays and arr[i] < arr[subArrays[-1]]:
                j = subArrays.pop()
                k = subArrays[-1] if subArrays else -1
                miniSum += arr[j] * (i - j) * (j - k)
            subArrays.append(i)

        while subArrays:
            j = subArrays.pop()
            k = subArrays[-1] if subArrays else -1
            miniSum += arr[j] * (len(arr) - j) * (j - k)

        return miniSum % modulo