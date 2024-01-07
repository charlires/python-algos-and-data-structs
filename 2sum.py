from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}
        for i in range(len(nums)):
            if (target - nums[i]) in prevMap:
                return [prevMap[target - nums[i]], i]
            prevMap[nums[i]] = i
        return [0, 0]
    
assert Solution().twoSum([3, 4, 5, 6, 1], 7) == [0, 1]
assert Solution().twoSum([4, 5, 6, 1], 7) == [2, 3]
