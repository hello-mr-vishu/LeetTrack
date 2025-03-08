class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = prices[0]
        cur_price = 0
        max_price  = 0
        for i in range(1,len(prices)):
            if buy_price > prices[i]:
                buy_price = prices[i]
            cur_price =  prices[i]- buy_price
            max_price = max(cur_price,max_price)
            cur_price = 0
        return max_price