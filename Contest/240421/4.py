from collections import defaultdict, deque
import heapq


class Solution:
    def findAnswer(self, n: int, edges: List[List[int]]) -> List[bool]:
        d = defaultdict(dict)
        ans = [float('inf') for _ in range(n)]
        walks = []
        for idx, e in enumerate(edges):
            f, s, path = e[0], e[1], e[2]
            d[s].update({f: [path, idx]})
            d[f].update({s: [path, idx]})
        heap = [[0, 0, []]]
        while heap:
            time, node, steps = heapq.heappop(heap)
            if ans[node] < time:
                continue
            ans[node] = time
            if node == n - 1:
                walks.append(steps)
                continue
            for next_node, info in d[node].items():
                new = steps + [info[1]]
                if info[0] + time > ans[next_node]:
                    continue
                heapq.heappush(heap, [time + info[0], next_node, new])
        seen = [False for _ in range(len(edges))]
        for walk in walks:
            for e in walk:
                seen[e] = True
        return seen
