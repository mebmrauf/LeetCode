# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0

        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        trappedWater = 0

        while left < right:
            leftMax = max(leftMax, height[left])
            rightMax = max(rightMax, height[right])

            if leftMax < rightMax:
                trappedWater += max(0, leftMax - height[left])
                left += 1
            else:
                trappedWater += max(0, rightMax - height[right])
                right -= 1

        return trappedWater