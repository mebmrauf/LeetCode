# 2108. Find First Palindromic String in the Array
# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            i, j = 0, len(word)-1
            while i < j:
                if word[i] != word[j]:
                    break
                else:
                    i, j = i+1, j-1
            if i >= j:
                return word
        return ''