class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        a = [0] * 26

        for ch in s:
            a[ord(ch)-ord('a')]+=1

        for ch in t:
            a[ord(ch)-ord('a')]-=1
        
        return all(x == 0 for x in a)