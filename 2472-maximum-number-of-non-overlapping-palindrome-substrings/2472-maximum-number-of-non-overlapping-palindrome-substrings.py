class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        res = 0
        n = len(s)
        start_from = 0

        for i in range(n):

            # j is the starting index
            for j in range(start_from, i - k + 2):

                if s[j:i+1] == s[j:i+1][::-1]:
                    res += 1
                    start_from = i + 1
                    break

        return res