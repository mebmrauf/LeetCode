# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, result, sets = 0, 0, set()
        for right in range(len(s)):
            while s[right] in sets:
                sets.remove(s[left])
                left += 1
            sets.add(s[right])
            result = max(result, right - left + 1)

        return result