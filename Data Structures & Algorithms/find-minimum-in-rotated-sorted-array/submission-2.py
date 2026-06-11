class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        while (l < r):
            m = (l+r)>>1
            print(f"l: {l} m: {m}: r: {r} val: {nums[m]}")
            if (nums[m] >= nums[r]):
                l = m + 1
            else:
                r = m
        return nums[l]