class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_value=float('inf')
        max_p=0
        for i in prices:
            if i<min_value:
                min_value=i
            else:
                p=i-min_value
                if p>max_p:
                    max_p=p
        return max_p