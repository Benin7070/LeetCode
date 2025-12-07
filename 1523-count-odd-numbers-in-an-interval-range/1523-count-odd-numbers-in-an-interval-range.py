class Solution:
    def countOdds(self, low: int, high: int) -> int:
        odd=(high+1)//2-low//2
        return odd