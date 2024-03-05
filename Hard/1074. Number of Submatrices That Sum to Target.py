# 1074. Number of Submatrices That Sum to Target
# https://leetcode.com/problems/number-of-submatrices-that-sum-to-target/description/

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        def subarraySum(nums: List[int], k: int) -> int:
            mp = Counter([0])
            count = pre = 0
            for x in nums:
                pre += x
                if pre - k in mp:
                    count += mp[pre - k]
                mp[pre] += 1
            return count
        
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            total = [0] * n
            for j in range(i, m):
                for c in range(n):
                    total[c] += matrix[j][c]
                ans += subarraySum(total, target)
        
        return ans