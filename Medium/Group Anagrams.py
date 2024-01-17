# 49. Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# https://leetcode.com/problems/group-anagrams/solutions/4584034/anagram-grouping-solution-in-python

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictAnagrams = {}
        for word in strs:
            anagram = ''.join(sorted(word))
            if anagram in dictAnagrams:
                dictAnagrams[anagram].append(word)
            else:
                dictAnagrams[anagram] = [word]
                
        return list(dictAnagrams.values())