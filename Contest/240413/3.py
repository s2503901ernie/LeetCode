from collections import defaultdict, deque


class Solution:
    def minimumTime(self, n: int, edges: List[List[int]], disappear: List[int]) -> List[int]:
        if disappear[0] == 0:
            return [-1 for _ in range(n)]
        d = defaultdict(dict)
        ans = [float('inf') for _ in range(n)]
        for e in edges:
            if e[1] in d[e[0]]:
                d[e[0]][e[1]] = min(e[2], d[e[0]][e[1]])
            else:
                d[e[0]].update({e[1]: e[2]})
            if e[0] in d[e[1]]:
                d[e[1]][e[0]] = min(e[2], d[e[1]][e[0]])
            else:
                d[e[1]].update({e[0]: e[2]})
        self.dfs(0, d, disappear, 0, ans)
        for i in range(len(ans)):
            if ans[i] == float('inf'):
                ans[i] = -1
        return ans


    def dfs(self, cur, d, disappear, time, ans):
        if disappear[cur] <= time:
            return
        if ans[cur] < time:
            return
        ans[cur] = time
        for node, need_time in d[cur].items():
            self.dfs(node, d, disappear, time + need_time, ans)





