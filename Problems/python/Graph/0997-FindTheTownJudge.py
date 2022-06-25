"""
In a town, there are n people labeled from 1 to n. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given an array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.



Example 1:

Input: n = 2, trust = [[1,2]]
Output: 2
Example 2:

Input: n = 3, trust = [[1,3],[2,3]]
Output: 3
Example 3:

Input: n = 3, trust = [[1,3],[2,3],[3,1]]
Output: -1


Constraints:

1 <= n <= 1000
0 <= trust.length <= 10^4
trust[i].length == 2
All the pairs of trust are unique.
ai != bi
1 <= ai, bi <= n
"""
from typing import List


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n == 1 and not trust:
            return 1
        judge = [[] for _ in range(n + 1)]
        trust_others = [-1 for _ in range(n + 1)]
        for t in trust:
            trust_others[t[0]] = 1
            judge[t[1]].append(t[0])
        ans = -1
        for i in range(1, n + 1):
            if trust_others[i] == -1 and len(judge[i]) == n - 1:
                ans = i

        return ans


class Solution1:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        ans = [0 for _ in range(n + 1)]
        for t in trust:
            ans[t[1]] += 1
            ans[t[0]] -= 1
        for i in range(1, n + 1):
            if ans[i] == n - 1:
                return i
            
        return -1
