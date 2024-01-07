class Solution:
    def bestProfit(self, prices: list[int]) -> int:
        maxprofit = 0
        l = 0 
        r = 1
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
                maxprofit = max(maxprofit, prices[r] - prices[l])
            r += 1
        return maxprofit
    

assert Solution().bestProfit([7,1,5,3,6,4]), 5
assert Solution().bestProfit([7,3,5,1,6,4]), 5