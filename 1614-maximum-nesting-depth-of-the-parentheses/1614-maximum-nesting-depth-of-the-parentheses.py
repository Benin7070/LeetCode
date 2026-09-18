class Solution:
    def maxDepth(self, s: str) -> int:
        max_nesting=0
        curr_nesting=0
        for i in s:
            if i=="(":
                curr_nesting+=1
                max_nesting=max(curr_nesting,max_nesting)
            elif i==")":
                curr_nesting-=1
        return max_nesting
