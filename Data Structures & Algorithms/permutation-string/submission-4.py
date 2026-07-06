class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        n1, n2 = len(s1), len(s2)
        need = [0] * 26
        window = [0] * 26
        
        for ch in s1:
            need[ord(ch) - ord('a')] += 1
        
        for i in range(n1):
            window[ord(s2[i]) - ord('a')] += 1
        
        if window == need:
            return True
        
        for i in range(n1, n2):
            window[ord(s2[i]) - ord('a')] += 1
            window[ord(s2[i - n1]) - ord('a')] -= 1
            if window == need:
                return True
        
        return False