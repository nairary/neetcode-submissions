class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)

        longest = 0
        for num in nums_set:
            if num-1 not in nums_set:
                current_streak = 1
                cur = num+1
                while cur in nums_set:
                    current_streak+=1
                    cur+=1
                longest = max(longest, current_streak)

        return longest