# 791. Custom Sort String
# https://leetcode.com/problems/custom-sort-string/

# Time complexity O(n*n)
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result = ''
        for i in order:
            if i in s:
                result += i*(s.count(i))
        
        for j in s:
            if j not in result:
                result += j*(s.count(j))
                
        return result

# Time complexity O(n)    
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        result, dicT = '', {}
        for i in s:
            if i not in dicT:
                dicT[i] = 1
            else:
                dicT[i] += 1

        for i in order:
            if i in dicT:
                result += i*dicT[i]
                del dicT[i]
        for key, val  in dicT.items():
            result += key*val
                
        return result