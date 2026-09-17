class Solution:
    def minSumOfLengths(self, arr: list[int], target: int) -> int:
        n = len(arr)

        best = [float('inf')] * n
        ans = float('inf')
        curr_sum = 0
        l = 0
        
        for r in range(n):
            curr_sum += arr[r]
            while curr_sum > target:
                curr_sum -= arr[l]
                l += 1
                
            if curr_sum == target:
                curr_len = r - l + 1

                if l > 0 and best[l - 1] != float('inf'):
                    ans = min(ans, best[l - 1] + curr_len)
                
                best[r] = curr_len
            if r > 0:
                best[r] = min(best[r], best[r - 1])
                
        return ans if ans != float('inf') else -1
