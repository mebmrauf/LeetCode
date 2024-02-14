# 2149. Rearrange Array Elements by Sign
# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        l = len(nums)
        pArr, nArr, pIndex, nIndex = [0]*(l//2), [0]*(l//2), 0, 0

        for i in nums:
            if i < 0:
                nArr[nIndex] = i
                nIndex += 1
            else:
                pArr[pIndex] = i
                pIndex += 1

        result, index, idx = [0]*l, 0, 0
        while index < l:
            result[index] = pArr[idx]
            index += 1
            result[index] = nArr[idx]
            index, idx = index + 1, idx + 1
        return result