"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        class UF:
            def __init__(self, n):
                self.p = [i for i in range(n)]

            def find(self, x):
                if x != self.p[x]:
                    self.p[x] = self.find(self.p[x])
                return self.p[x]

            def union(self, x, y):
                self.p[self.find(x)] = self.find(y)

        uf = UF(len(nums))
        d = {}
        for i in range(len(nums)):
            if nums[i] - 1 in d:
                uf.union(i, d[nums[i] - 1])
            if nums[i] + 1 in d:
                uf.union(i, d[nums[i] + 1])
            d[nums[i]] = i

        seen = {}

        for i in range(len(nums)):
            if uf.find(i) not in seen:
                seen[uf.find(i)] = {nums[i]}
            else:
                seen[uf.find(i)].add(nums[i])
        ans = 0
        for _, v in seen.items():
            ans = max(ans, len(v))

        return ans
