# 217. Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setOfnums = set()
        for num in nums:
            if num not in setOfnums:
                setOfnums.add(num)
            else:
                return True
        return False
    
# OR
    
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = Counter(nums)
        occur = list(count.values())
        return not([1]*len(occur) == occur)