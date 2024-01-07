from typing import List
import heapq

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for n in s: 
            if n-1 in s:
                continue

            count = 1
            next = n+1
            while next in s:
                next += 1
                count += 1
            longest = max(count, longest)

        return longest
            
        # heapq.heapify(nums)
        # prev = None
        # count = 0
        # longest = 0
        # while len(nums):
        #     num = heapq.heappop(nums)
        #     if prev is not None and num - prev == 1:
        #         count += 1
        #     elif num == prev:
        #         pass
        #     else: 
        #         count = 1
        #     longest = max(longest, count)
        #     prev = num

        # return longest
    
print(Solution().longestConsecutive([100,4,200,1,3,2]))
print(Solution().longestConsecutive([0,3,7,2,5,8,4,6,0,1]))
print(Solution().longestConsecutive([1,2,0,1]))