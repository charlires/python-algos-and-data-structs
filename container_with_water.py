class Solution:
    def maxArea(self, height: list[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxwater = 0 
        while l < r:
            maxwater = max(min(height[l], height[r]) * (r-l), maxwater)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return maxwater