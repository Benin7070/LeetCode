class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations=sorted(citations,reverse=True)
        for i in range(len(citations)):
            if citations[i]<i+1:
                return i
                break
        return len(citations)
