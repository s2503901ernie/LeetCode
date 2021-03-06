"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.



Example 1:


Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2
Example 2:


Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
Output: 3


Constraints:

1 <= n <= 200
n == isConnected.length
n == isConnected[i].length
isConnected[i][j] is 1 or 0.
isConnected[i][i] == 1
isConnected[i][j] == isConnected[j][i]
"""
from typing import List


class Solution:
    """ Union """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        p = [i for i in range(len(isConnected))]
        b = {}
        ans = 0

        def union(parent, child):
            p[find(child)] = find(parent)

        def find(x):
            if x != p[x]:
                p[x] = find(p[x])

            return p[x]

        for i in range(len(isConnected)):
            for j in range(len(isConnected[i])):
                if j == i or isConnected[i][j] == 0:
                    continue
                union(i, j)

        for i in p:
            if find(i) not in b:
                ans += 1
                b[find(i)] = True

        return ans


class Solution2:
    """ DFS """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        b = {}
        ans = 0
        def dfs(idx):
            for i in range(len(isConnected[idx])):
                if i not in b and isConnected[idx][i] == 1:
                    b[i] = True
                    dfs(i)

        for i in range(len(isConnected)):
            if i not in b:
                dfs(i)
                ans += 1

        return ans


class Solution3:
    """ BFS """
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        b = {}
        ans = 0

        def bfs(i):
            if i in b:
                return 0
            stack = [i]
            while stack:
                idx = stack.pop()
                cur = isConnected[idx]
                if idx in b:
                    continue
                b[idx] = 1
                for i in range(len(cur)):
                    if i == idx or i in b or cur[i] == 0:
                        continue
                    stack.append(i)

            return 1

        for i in range(len(isConnected)):
            ans += bfs(i)
        return ans
