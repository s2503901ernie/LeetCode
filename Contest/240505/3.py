from collections import deque
from collections import defaultdict


class Solution:
    def minAnagramLength(self, s: str) -> int:
        l = 1
        ans = float('inf')
        r = len(s)
        n = len(s)
        while l <= r:
            if n % l != 0:
                l += 1
                continue
            d0 = defaultdict(int)
            valid = True
            for i in range(0, n, l):
                d = defaultdict(int)
                if i == 0:
                    for c in s[i:i+l]:
                        d0[c] += 1
                    continue
                else:
                    for c in s[i:i+l]:
                        d[c] += 1
                if d0 != d:
                    valid = False
                    break
            if valid:
                ans = min(ans, l)
            l += 1
        return ans



