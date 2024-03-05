# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements

# Time Complexity - O(n log n)
class Solution:
    def topKFrequent(self, nums, k):
        counter = Counter(nums)
        frequent_elements = counter.most_common(k)
        result = [element for element, _ in frequent_elements]
        
        return result
    
# Time Complexity - O(n)  
class Solution:
    def topKFrequent(self, nums, k):
        count = Counter(nums)

        sfList = [[] for _ in range(len(nums) + 1)]
        
        for num, occur in count.items():
            sfList[occur].append(num)

        fList = []
        for bucket in reversed(sfList):
            fList.extend(bucket)
            if len(fList) >= k:
                break
        
        return fList[:k]