from typing import List

class Solution: 
    def findMatch(self, nums: List[int], target: int):

        def match(i, result):
            if i == len(nums):
                return target == result
            
            return match(i+1, nums[i] + result) or match(i+1, nums[i] * result)
        
        return match(1, nums[0] + 0) or match(1, nums[0] * 1)

assert Solution().findMatch([1, 2, 3], 6) == True
assert Solution().findMatch([1, 1, 1], 0) == False
assert Solution().findMatch([-1, 1, -1], 1) == True