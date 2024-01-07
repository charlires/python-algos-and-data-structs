from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        counter = 0
        for i in range(len(nums)-2): 
            j = len(nums)-1
            while j > i:
                sub = nums[j] - nums[i]
                if sub > diff: 
                    j -= 1
                    continue
                elif sub == diff:
                    k = len(nums)-1
                    while k > j: 
                        sub = nums[k] - nums[j]
                        if sub > diff: 
                            k -= 1
                            continue
                        elif sub == diff: 
                            counter += 1
                        break
                    j = i
                break
                    
        return counter
    
print(Solution().arithmeticTriplets([0,1,4,6,7,10], 3))
print(Solution().arithmeticTriplets([4,5,6,7,8,9], 2))

