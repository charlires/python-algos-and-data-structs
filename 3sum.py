from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = a + nums[l] + nums[r]
                if sum < 0:
                    l += 1
                elif sum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
         # nums.sort()
        # result = []
        # s = set()
        # c = 0

        # while c < len(nums) - 1:
        #     if nums[c] in s:
        #         c += 1
        #         continue

        #     l, r = c + 1, len(nums) - 1
        #     while l < r:
        #         if nums[c] + nums[l] + nums[r] < 0:
        #             l += 1 
        #         elif nums[c] + nums[l] + nums[r] > 0:
        #             r -= 1
        #         else: 
        #             result.append([nums[c], nums[l], nums[r]])
        #             s.add(nums[c])
        #             break
        #     c += 1
            

        # return result

# print(Solution().threeSum([-3, -3, 2, 4, 5, 1, 2]))
print(Solution().threeSum([-1,0,1,2,-1,-4]))
-1, 0, 1