"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.



Example 1:


Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
Example 2:

Input: n = 2, connections = [[0,1]]
Output: [[0,1]]


Constraints:

2 <= n <= 10^5
n - 1 <= connections.length <= 10^5
0 <= ai, bi <= n - 1
ai != bi
There are no repeated connections.
"""
from typing import List


class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]
        rank = [i for i in range(n)]
        ans = []
        cur = 0
        prev = -1
        for edge in connections:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        self.dfs(cur, prev, graph, ans, visited, rank, 0)

        return ans

    def dfs(self, cur, prev, graph, ans, visited, rank, cur_rank):
        visited[cur] = True
        rank[cur] = cur_rank
        for node in graph[cur]:
            if node == prev:
                continue
            if visited[node] is False:
                self.dfs(node, cur, graph, ans, visited, rank, cur_rank + 1)
            rank[cur] = min(rank[cur], rank[node])
            if cur_rank < rank[node]:
                ans.append([cur, node])

