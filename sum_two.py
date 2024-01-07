class Solution: 
    def sumTwo(self, nums: list[int], target: int):
        # map = {}
        com = set()
        for i in nums:
            if i in com:#map:
                return True
            com.add(target -i)
            # map[target - i] = i
        return False
        # i = 0 
        # j = len(nums) -1
        # while i != j:
        #     if nums[i] + nums[j] == target:
        #         return True
            
        # return False
    
print(Solution().sumTwo([1, 2, 3, 4, 4], 8))