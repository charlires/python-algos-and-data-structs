from typing import List

class Solution: 
     def bubbleSort(self, nums: List[int]) -> List[int]:
          for i in range(len(nums)):
               for j in range(len(nums) - 1 - i):
                    if nums[j] > nums[j + 1]:
                         temp = nums[j]
                         nums[j] = nums[j + 1]
                         nums[j + 1] = temp
          return nums
     
print(Solution().bubbleSort([5, 4, 6, 7, 9, 1, 2, 5]))