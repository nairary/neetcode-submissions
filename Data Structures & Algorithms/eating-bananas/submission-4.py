from typing import List
class Solution:
    def tookHours(self, piles: List[int], v: int) -> int:
        time = 0
        for pile in piles:
            a = pile // v
            if (a < 1):
                time += 1
            else:
                if (pile % (a * v) > 0):
                    time += a + 1
                else:
                    time += a
        print(f"v: {v}, time: {time}")
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = 1000000000
        l = 1
        while(l<=r):
            m = ((r+l)>>1)
            time = self.tookHours(piles, m)
            if (time <= h):
                r = m-1
            elif (time > h):
                l = m+1
            print(f"l: {l}, m: {m}, r: {r}")
        return l
            
piles = [1, 4, 3, 2]
h = 9

sol = Solution()
print(sol.minEatingSpeed(piles, h))