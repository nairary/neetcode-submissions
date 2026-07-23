class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        result = 100000
        for i in range(len(nums)-k+1):
            result = min(result, nums[i+k-1]-nums[i])
        return result