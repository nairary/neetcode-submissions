class Solution:
    def canJump(self, nums: List[int]) -> bool:
        counter = 0
        n = len(nums)
        i = n-1
        while i > 0:
            counter+=1
            i-=1

            if nums[i] >= counter:
                counter = 0
        
        return (counter == 0)