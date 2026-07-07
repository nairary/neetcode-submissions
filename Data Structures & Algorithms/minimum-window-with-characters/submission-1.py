class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        
        need = {}
        for ch in t:
            need[ch] = need.get(ch, 0) + 1
        
        min_len = float('inf')
        min_start = ""
        missing = len(need)
        l, r = 0, 0
        while r < len(s):
            ch = s[r]
            if ch in need:
                need[ch]-=1
                if need[ch] == 0:
                    missing-=1
            
            while missing == 0:
                if min_len > r-l+1:
                    min_len = r-l+1
                    min_start = l
                
                if s[l] in need:
                    need[s[l]] += 1
                    if need[s[l]] > 0:
                        missing += 1
            
                l+=1
            r+=1
        
        return "" if min_len == float('inf') else s[min_start:min_start+min_len]

