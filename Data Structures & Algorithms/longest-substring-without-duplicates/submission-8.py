class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        
        l, r = 0, 1
        result = 0
        hash_set = set()
        hash_set.add(s[l])
        while r < len(s):
            if s[r] in hash_set:
                while s[l] != s[r]:
                    hash_set.remove(s[l])
                    l+=1
                hash_set.remove(s[l])
                l+=1

            hash_set.add(s[r])
            result = max(result, len(hash_set))
            r+=1
        
        return result