class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        result = 0
        window = 0
        for i in range(k):
            window+=arr[i]
        print(window)
        if window >= threshold*k:
            result+=1
        l = 0
        r = k
        while r < len(arr):
            print(f"{window} + {arr[r]} - {arr[l]} = {window+arr[r]-arr[l]}")
            window+=arr[r]
            window-=arr[l]
            r+=1
            l+=1
            if window >= threshold*k:
                result+=1
        return result
