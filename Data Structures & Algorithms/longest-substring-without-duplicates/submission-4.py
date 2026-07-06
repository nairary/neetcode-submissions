class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 0:
            return len(s)

        l, r = 0, 1
        set_map = set()
        result = 1
        while r < len(s):
            set_map.add(s[l])
            if s[r] not in set_map:
                set_map.add(s[r])
                r+=1
            else:
                set_map.remove(s[l])
                result=max(result, r-l)
                l+=1
                if l == r:
                    r+=1
        return max(result, r-l)
