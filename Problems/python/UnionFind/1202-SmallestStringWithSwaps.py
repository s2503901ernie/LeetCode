"""
You are given a string s, and an array of pairs of indices in the string pairs where pairs[i] = [a, b] indicates 2 indices(0-indexed) of the string.

You can swap the characters at any pair of indices in the given pairs any number of times.

Return the lexicographically smallest string that s can be changed to after using the swaps.



Example 1:

Input: s = "dcab", pairs = [[0,3],[1,2]]
Output: "bacd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[1] and s[2], s = "bacd"
Example 2:

Input: s = "dcab", pairs = [[0,3],[1,2],[0,2]]
Output: "abcd"
Explaination:
Swap s[0] and s[3], s = "bcad"
Swap s[0] and s[2], s = "acbd"
Swap s[1] and s[2], s = "abcd"
Example 3:

Input: s = "cba", pairs = [[0,1],[1,2]]
Output: "abc"
Explaination:
Swap s[0] and s[1], s = "bca"
Swap s[1] and s[2], s = "bac"
Swap s[0] and s[1], s = "abc"


Constraints:

1 <= s.length <= 10^5
0 <= pairs.length <= 10^5
0 <= pairs[i][0], pairs[i][1] < s.length
s only contains lower case English letters.
"""
from typing import List


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        class UF:
            def __init__(self, n):
                self.p = list(range(n))

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]
        uf = UF(len(s))
        res = []
        m = dict()
        for x, y in pairs:
            uf.union(x, y)
        for i in range(len(s)):
            if uf.find(i) not in m:
                m[uf.find(i)] = [s[i]]
            else:
                m[uf.find(i)].append(s[i])

        for key in m.keys():
            m[key].sort(reverse=True)

        for i in range(len(s)):
            res.append(m[uf.find(i)].pop())

        return ''.join(res)
