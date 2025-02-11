# 1910. Remove All Occurrences of a Substring
# https://leetcode.com/problems/remove-all-occurrences-of-a-substring/

# Using Stack
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack, leng = [], len(part)

        for i in s:
            stack.append(i)

            if len(stack) >= leng and ''.join(stack[-leng:]) == part:
                del stack[-leng:]

        return ''.join(stack)

# Using String Replace    
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while part in s:
            s = s.replace(part, "", 1)
        return s

# Using String Find    
class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        while True:
            index = s.find(part)
            if index == -1:
                break
            s = s[:index]+s[index+len(part):]
        return s