class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sufix = [0]*len(nums)
        prefix = [0]*len(nums)

        prefix[0] =  1
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1]*nums[i-1]

        sufix[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            sufix[i] = sufix[i+1] * nums[i+1]

        return [x*y for x, y in zip(sufix, prefix)]