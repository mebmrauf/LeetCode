# 2966. Divide Array Into Arrays With Max Difference
# https://leetcode.com/problems/divide-array-into-arrays-with-max-difference/description/

class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        
        for i in range(0, len(nums), 3):
            if i + 2 > len(nums) or nums[i+2] - nums[i] > k:
                return []    
            else:
                result.append(nums[i:i+3])
                
        return result