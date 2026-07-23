class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        threshold*=k
        r = 0
        window = 0
        result = 0
        for r in range(len(arr)):
            window+=arr[r]
            if r-k+1>=0:
                result += window >= threshold
                window-=arr[r-k+1]
        return result