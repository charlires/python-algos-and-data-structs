from typing import List

# the list of nums is already sorted in ascending order
# return index starting with 1 and not 0
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i < j: 
            if (nums[i] + nums[j]) > target:
                j -= 1
            elif (nums[i] + nums[j]) < target:
                i += 1
            else: 
                return [i+1, j+1]    
        return [0, 0]
print(Solution().twoSum([1, 3, 4, 5, 7, 10, 11], 9))
assert Solution().twoSum([1, 3, 4, 5, 7, 10, 11], 9) == [3, 4]
    
# assert Solution().twoSum([3, 4, 5, 6, 1], 7) == [0, 1]
# assert Solution().twoSum([4, 5, 6, 1], 7) == [2, 3]
