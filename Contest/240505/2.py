from collections import deque
from collections import defaultdict


class Solution:
    def minimumOperationsToMakeKPeriodic(self, word: str, k: int) -> int:
        d = defaultdict(int)
        for i in range(0, len(word), k):
            d[word[i:i+k]] += 1
        max_val = 0
        w = None
        for k, v in d.items():
            if v > max_val:
                w = k
                max_val = max(v, max_val)
        ans = 0
        for k, v in d.items():
            if k != w:
                ans += v
        return ans


