class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        result = 100
    
        count = 0
        for i in range(k):
            if blocks[i] == 'W':
                count+=1
        
        result = min(result, count)
        l, r = 0, k-1
        while r < len(blocks) - 1:
            if blocks[l] == 'W':
                count-=1
            l+=1
            r+=1
            if blocks[r] == 'W':
                count+=1
            result = min(result, count)

        return result