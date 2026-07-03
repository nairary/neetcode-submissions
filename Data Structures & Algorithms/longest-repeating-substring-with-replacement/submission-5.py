class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqs = {}
        maxf = 0
        l = 0
        result = 0
        for r in range(len(s)):
            freqs[s[r]] = freqs.get(s[r], 0) + 1
            maxf = max(maxf, freqs[s[r]])

            while (r-l+1 - maxf > k):
                freqs[s[l]] -= 1
                l+=1
                
            result = max(result, r-l+1)
        return result