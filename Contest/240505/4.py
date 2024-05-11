from collections import deque
from collections import defaultdict


class Solution:
    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        t = nums[-1]
        t2 = t * 2
        ans = float('inf')
        array = nums.copy()
        while t <= t2:
            cur = 0
            nums = array.copy()
            while 0 <= r:
                if r >= 1:
                    n1, n2 = nums[r - 1], nums[r]
                    if cost1 * 2 < cost2:
                        cur += (t - n2) * cost1
                        cur += (t - n1) * cost1
                        r -= 2
                        continue
                    cur += (t - n2) * cost2
                    nums[r - 1] += (t - n2)
                    r -= 1
                    continue
                cur += (t - nums[0]) * cost1
                r -= 1
            print(cur)
            t += 1
            r = len(nums) - 1
            ans = min(ans, cur)
        return ans

