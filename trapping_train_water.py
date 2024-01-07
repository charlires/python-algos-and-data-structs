class Solution:
    def trap(self, height: list[int]) -> int:
        l = 0
        r = len(height) -1
        lmax = height[l]
        rmax = height[r]
        water = 0
        while l < r:
            if lmax < rmax:
                l += 1
                if lmax < height[l]:
                    lmax = height[l]
                else:
                    water += lmax - height[l]
            else: 
                r -= 1
                if rmax < height[r]:
                    rmax = height[r]
                else:
                    water += rmax - height[r]
        return water
        # pass

assert Solution().trap([0,2,0]) == 0, "all zero"
assert Solution().trap([0,0,0,0,0]) == 0, "all zero"
assert Solution().trap([0,1,0,2]) == 1, "water 1"
assert Solution().trap([0,1,0,2,1,0,1,3]) == 5, "water 5"
assert Solution().trap([0,1,0,3,0,1]) == 2, "water 2"
assert Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]) == 6, "water 6"