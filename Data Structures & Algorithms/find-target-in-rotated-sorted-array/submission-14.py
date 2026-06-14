class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        while (l<r):
            m = (l+r)>>1
            if (nums[m] >= nums[r]):
            # левая половина отсортирована
                if (nums[l] <= target <= nums[m]):
                    r = m
                else:
                    l = m+1
            else:
            # правая половина отсортирована
                if (nums[m] < target <= nums[r]):
                    l = m+1
                else:
                    r = m
        if (nums[l] == target):
            return l
        else:
            return -1
            