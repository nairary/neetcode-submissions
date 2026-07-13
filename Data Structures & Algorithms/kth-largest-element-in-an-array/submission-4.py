class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        index = n - k
            
        p = 0
        l, r = 0, n-1
        while True:
            p = l
            pivot = nums[r]
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[i], nums[p] = nums[p], nums[i]
                    p+=1
            nums[p], nums[r] = nums[r], nums[p]

            if p < index:
                l = p + 1
            elif p > index:
                r = p - 1
            else:
                return nums[p]
                