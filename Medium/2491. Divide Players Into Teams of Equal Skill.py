# 2491. Divide Players Into Teams of Equal Skill
# https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

# Time Complexity O(nlogn)
from typing import List
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        totalSkill = skill[0] + skill[-1]
        chemistry, left, right = 0, 0, n - 1
        
        while left < right:
            if skill[left] + skill[right] != totalSkill:
                return -1
            chemistry += (skill[left] * skill[right])
            left, right = left +1, right -1
        
        return chemistry