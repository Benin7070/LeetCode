class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=float('inf')
        max_profit=0
        for i in prices:
            if i<min_value:
                min_value=i
            elif i>min_value:
                max_profit=max(max_profit,i-min_value)
        return max_profit
