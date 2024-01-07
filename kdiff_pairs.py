from typing import List
import collections

class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        total = 0
        count = 0
        c = collections.Counter()        
        for i, x in enumerate(nums):
            count += c[k - abs(x)]
            total += i
            c[k - abs(x)] += 1
        return total - count

            # if 
            # for j in range(i+1, len(nums)):
                # if abs(nums[i] - nums[j]) == k:
                    # if (nums[i], nums[j]) not in s and (nums[j], nums[i]) not in s:
                        # s.add((nums[i], nums[j]))
                        # s.add((nums[j], nums[i]))
                        # count += 1
        # return count

print(Solution().findPairs([3,1,4,1,5], 2))