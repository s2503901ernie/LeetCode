"""
Given two integers n and k, return all possible combinations of k numbers out of the range [1, n].

You may return the answer in any order.



Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]


Constraints:

1 <= n <= 20
1 <= k <= n
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        self.helper(1, n, k, [], ans)

        return ans

    def helper(self, start, n, k, cur, ans):
        if len(cur) == k:
            ans.append(cur)
            return
        elif len(cur) > k:
            return
        for i in range(start, n + 1):
            new = cur + [i]
            self.helper(i + 1, n, k, new, ans)
