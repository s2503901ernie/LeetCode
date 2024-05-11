import heapq


class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        s = set()
        l = []
        for c in coins:
            cur = 0
            for i in range(1, k + 1):
                cur += c
                if cur in s:
                    continue
                s.add(cur)
                heapq.heappush(l, cur)
        print(l)
        for _ in range(k):
            ans = heapq.heappop(l)
        return ans

