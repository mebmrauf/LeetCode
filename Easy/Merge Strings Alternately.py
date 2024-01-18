# 1768. Merge Strings Alternately
# https://leetcode.com/problems/merge-strings-alternately

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index, finalStr = min(len(word1), len(word2)), ''
        for i in range(index):
            finalStr = finalStr + word1[i] + word2[i]
        finalStr = finalStr + word1[index:] + word2[index:]
        return finalStr