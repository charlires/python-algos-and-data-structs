from typing import List


class Solution:

    def __init__(self, picked: int) -> None:
        self.picked = picked

    def guess(self, num: int) -> int:
        if num > self.picked:
            return -1
        elif num < self.picked:
            return 1
        elif num == self.picked:
            return 0 

    def guessNumber(self, nums: List[int]) ->  int:
        i, j = 0, len(nums) -1
        guess = j // 2
        while True:
            res = self.guess(nums[guess])
            if res == 0:
                return nums[guess]
            
            if res == -1:
                j = guess -1
            elif res == 1:
                i = guess +1
            guess = (j + i) // 2

# print(7 // 2)             
sol = Solution(3)
print(sol.guessNumber([1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]))
# sol.guess()
    
