class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}

        for i in s:
            freq[i]=freq.get(i,0)+1

        print(freq)

        res=""
        sorted_freq = dict(sorted(freq.items(), key=lambda item: (item[1], item[0]),reverse=True))

        for i in sorted_freq.items():
            res+=i[0]*i[1]

        return res