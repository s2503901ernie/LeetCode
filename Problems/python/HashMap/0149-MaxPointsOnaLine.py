"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-10^4 <= xi, yi <= 10^4
All the points are unique.
"""
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)):
            dic = {}
            cur = points[i]
            x, y = cur[0], cur[1]
            cur_max = 0
            for j in range(i+1, len(points)):
                nx, ny = points[j][0], points[j][1]
                dx = nx - x
                dy = ny - y
                if dx != 0:
                    dic[dy / dx] = dic.get(dy / dx, 0) + 1
                    cur_max = max(cur_max, dic[dy/dx])
                else:
                    dic['inf'] = dic.get('inf', 0) + 1
                    cur_max = max(cur_max, dic['inf'])
            ans = max(ans, cur_max + 1)

        return ans
