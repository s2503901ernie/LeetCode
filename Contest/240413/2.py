from collections import defaultdict, deque


class Solution:
    def minRectanglesToCoverPoints(self, points: List[List[int]], w: int) -> int:
        points = sorted(points, key=lambda x: x[0])
        ans = 0
        x = points[0][0]
        for p in points[1:]:
            px = p[0]
            if px - x > w:
                ans += 1
                x = px
        return ans + 1
