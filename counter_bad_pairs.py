from typing import List
import collections

class Solution: 
    def countBadPairs(self, nums: List[int]) -> int: 
        c = collections.Counter()
        total = 0
        match = 0
        for i, x in enumerate(nums): 
            match += c[i - x]
            total += i
            c[i - x] += 1
        return total - match


print(Solution().countBadPairs([1, 2, 3, 4, 5, 6, 8, 3]))