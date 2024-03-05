# 1750. Minimum Length of String After Deleting Similar Ends
# https://leetcode.com/problems/minimum-length-of-string-after-deleting-similar-ends/

class Solution:
    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1
        if s[left] != s[right]:
            return len(s)
        while left < right and s[left] == s[right]:
            alpha = s[left]
            while left <= right and s[left] == alpha: left += 1
            while left <= right and s[right] == alpha: right -= 1
        return right - left + 1