# 1207. Unique Number of Occurrences
# https://leetcode.com/problems/unique-number-of-occurrences/

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        noOfoccurences = Counter(arr)
        uniqueOccurences = set(noOfoccurences .values())
        return len(noOfoccurences ) == len(uniqueOccurences)