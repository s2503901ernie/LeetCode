"""
You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] = [xi, yi].

The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them: |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

Return the minimum cost to make all points connected. All points are connected if there is exactly one simple path between any two points.



Example 1:


Input: points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
Output: 20
Explanation:

We can connect the points as shown above to get the minimum cost of 20.
Notice that there is a unique path between every pair of points.

Example 2:

Input: points = [[3,12],[-2,5],[-4,1]]
Output: 18


Constraints:

1 <= points.length <= 1000
-10^6 <= xi, yi <= 10^6
All pairs (xi, yi) are distinct.
"""
import heapq
from typing import List


class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        adj = {i: [] for i in range(n)}
        for i in range(n):
            cur = points[i]
            for j in range(i+1, n):
                compared = points[j]
                dist = self.cal(cur, compared)
                adj[i].append([dist, j])
                adj[j].append([dist, i])
        print(adj)
        res = 0
        visit = set()
        heap = [[0, 0]]
        while len(visit) < n:
            cost, i = heapq.heappop(heap)
            if i in visit:
                continue
            res += cost
            visit.add(i)
            for nei_cost, nei in adj[i]:
                if nei not in visit:
                    heapq.heappush(heap, [nei_cost, nei])
        return res

    def cal(self, p1, p2):

        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
