# 125. Valid Palindrome
# https://leetcode.com/problems/valid-palindrome/

import re # No need to import in LeetCode

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub(r'[^a-z0-9]', '', s)
        left, right = 0, len(s)-1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True
    
# re.sub(r'[^a-zA-Z0-9]', '', input_string)
# effectively removes non-alphanumeric characters from the original string.