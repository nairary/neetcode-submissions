class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        l, r = 0, 1
        result = 1
        while l < len(s):
            hash_set = set()
            hash_set.add(s[l])
            local_result = 1
            while r < len(s) and s[r] not in hash_set:
                hash_set.add(s[r])
                local_result+=1
                r+=1
            result = max(result, local_result)
            l+=1
            r=l+1

        return result
        