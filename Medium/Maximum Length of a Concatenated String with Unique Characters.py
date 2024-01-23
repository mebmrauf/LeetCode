# 1239. Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

class Solution:
    def maxLength(self, arr: List[str]) -> int:
        distinct = ['']
        maxLen = 0
        for i in range(len(arr)):
            current = distinct
            for j in range(len(current)):
                newStr = arr[i] + current[j]
                if len(set(newStr)) == len(newStr):
                    distinct.append(newStr)
                    maxLen = max(maxLen, len(newStr))
        return maxLen