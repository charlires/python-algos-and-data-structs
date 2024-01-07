class Solution(object):
    def ensure_max_consecutive_duplicates(self, arr):
        if not arr:
            return arr

        result = [arr[0]]
        count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                count += 1
                if count <= 4:
                    result.append(arr[i])
            else:
                count = 1
                result.append(arr[i])

        return result
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        m = {}
        nums = sorted(self.ensure_max_consecutive_duplicates(nums))
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum in m:
                    m[sum].append([i, j])
                else:
                    m[sum] = [[i, j]]

        # for k in m:
        #     print(k, m[k])

        result = set()
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if (target - sum) in m:
                    for p in m[target - sum]:
                        if p[0] != i and p[0] != j and p[1] != i and p[1] != j:
                            r = tuple(sorted([nums[p[0]], nums[p[1]], nums[i], nums[j]]))
                            result.add(r)
        return list(list(r) for r in result)

solution = Solution()
# solution.fourSum([-4,-3,-2,-1,0,0,1,2,3,4], 0)
# print(solution.fourSum([-4,-3,-2,-1,0,0,1,2,3,4], 0))
print(solution.fourSum([10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,40,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,50,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,60,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,70,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,80,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90,90], 200))
print(solution.fourSum([2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2], 8))

# [-4,-1,1,4]