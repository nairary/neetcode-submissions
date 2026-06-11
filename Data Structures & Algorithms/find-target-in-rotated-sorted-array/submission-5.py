class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1
        m = 0
        while (l<r):
            m = (l+r)>>1
            print(f"l: {l} m: {m} r: {r} target: {target} nums[m]: {nums[m]}")
            if (nums[m] == target):
                return m
            elif (nums[m] > target):
                if (nums[m] > nums[r]):
                    if (nums[r] >= target):
                        l = m+1
                    else:
                        r = m-1
                    continue
                if (nums[m] < nums[r]):
                    r = m-1
                    continue
                return -1
            elif (nums[m] < target):
                if (nums[m] < nums[r]):
                    if (target <= nums[r]):
                        l = m + 1
                    else:
                        r = m - 1
                    continue
                if (nums[m] > nums[r]):
                    if (nums[l] < target):
                        l = m + 1
                    else:
                        r = m - 1
                    continue
                return -1
        if (nums[l] == target):
                return l
        else:
            return -1


