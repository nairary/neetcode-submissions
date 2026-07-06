class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        if len(s2) <= 1:
            return s1==s2
        
        n1 = len(s1)
        n2 = len(s2)
        l, r = 0, 0
        hash_map = dict()
        for ch in s1:
            hash_map[ch] = hash_map.get(ch, 0) + 1
        
        window = dict()
        while r < n2:
            while r-l+1 <= n1:
                print(r-l+1)
                window[s2[r]] = window.get(s2[r], 0) + 1
                r+=1
            
            print(f"window: {window}")
            print(f"hash_map: {hash_map}")
            if window == hash_map:
                return True
            else:
                window[s2[l]]-=1
                if window[s2[l]] == 0:
                    del window[s2[l]]
                l+=1

        return False