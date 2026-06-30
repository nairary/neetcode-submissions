class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()

        for i in range(0, len(nums)):
            rest = target - nums[i]
            if hash_map.get(rest, -1) != -1:
                return [hash_map.get(rest), i]
            else:
                hash_map[nums[i]] = i