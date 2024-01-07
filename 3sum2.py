from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        target = 0
        result = []

        lset = set()
        for l in range(len(nums) -2):
            if nums[l] in lset:
                continue

            m = l+1
            r = len(nums) -1
            rset = set([nums[r]])
            mset = set([nums[m]])
            while m < r: 
                sum = nums[l] + nums[m] + nums[r]
                if sum > target: 
                    r -= 1
                    while nums[r] in rset and m < r: 
                        r -= 1

                elif sum < target: 
                    m += 1
                    while nums[m] in mset and m < r: 
                        m += 1

                else: 
                    result.append([nums[l] ,nums[m] ,nums[r]])
                    m += 1
                    while nums[m] in mset and m < r: 
                        m += 1

                rset.add(nums[r])
                mset.add(nums[m])
            lset.add(nums[l])

        return result
    

    
# print(Solution().threeSum([0, 0, 0]))
print(Solution().threeSum([-1,0,1,0]))












