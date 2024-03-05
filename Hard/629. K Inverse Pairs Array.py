# 629. K Inverse Pairs Array
# https://leetcode.com/problems/k-inverse-pairs-array/description/

class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD, arr1 = 10**9 + 7, [1] + [0] * k
        
        for i in range(1, n + 1):
            arr2 = [0] * (k + 1)
            for j in range(k + 1):
                x = arr2[j - 1] if j - 1 >= 0 else 0
                y = arr1[j - i] if j - i >= 0 else 0
                arr2[j] = x - y + arr1[j]
                arr2[j] %= MOD
            arr1 = arr2
        
        return arr1[k]