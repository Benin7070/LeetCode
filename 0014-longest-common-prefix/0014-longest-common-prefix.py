class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        min_word=min(strs,key=len)
        for i in range(len(min_word)):
            for word in strs:
                if min_word[i]!=word[i]:
                    return min_word[:i]
        return min_word