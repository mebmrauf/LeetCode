# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/description/

class Solution:
    def frequencySort(self, s: str) -> str:
        appears, string = Counter(s).most_common(), ''
        for i in appears:
            string += i[0]*i[1]
        return string