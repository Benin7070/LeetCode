class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x>=0:
            return True if str(x)[::-1]==str(x) else False
        return False