class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        window_freq={}
        i=j=0
        res=0
        max_freq=0
        
        while j<len(s):

            window_freq[s[j]]=window_freq.get(s[j],0)+1
            curr_len=(j-i)+1
            max_freq=max(max_freq,window_freq[s[j]])

            if curr_len-max_freq<=k:
                res=max(res,curr_len)
                j+=1

            else:
                if True:
                    window_freq[s[j]]=window_freq.get(s[j],0)-1
                window_freq[s[i]]-=1
                i+=1

        return res