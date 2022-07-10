"""
You are given a 0-indexed integer array nums and an integer k.

You are initially standing at index 0. In one move, you can jump at most k steps forward without going outside the boundaries of the array. That is, you can jump from index i to any index in the range [i + 1, min(n - 1, i + k)] inclusive.

You want to reach the last index of the array (index n - 1). Your score is the sum of all nums[j] for each index j you visited in the array.

Return the maximum score you can get.



Example 1:

Input: nums = [1,-1,-2,4,-7,3], k = 2
Output: 7
Explanation: You can choose your jumps forming the subsequence [1,-1,4,3] (underlined above). The sum is 7.
Example 2:

Input: nums = [10,-5,-2,4,0,3], k = 3
Output: 17
Explanation: You can choose your jumps forming the subsequence [10,4,3] (underlined above). The sum is 17.
Example 3:

Input: nums = [1,-5,-20,4,-1,3,-6,-3], k = 2
Output: 0


Constraints:

1 <= nums.length, k <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List
import heapq


class Solution:
    """dfs, TLE"""
    def maxResult(self, nums: List[int], k: int) -> int:
        self.ans = -float('inf')
        self.dfs(nums, 0, 0, k)

        return self.ans

    def dfs(self, nums, cur, p, k):
        if p >= len(nums):
            return
        for i in range(p, p + k):
            new = cur + nums[i]
            if i == len(nums) - 1:
                self.ans = max(self.ans, new)
                return
            elif i < len(nums) - 1:
                self.dfs(nums, new, i + 1, k)


class Solution2:
    """DP, TLE"""
    def maxResult(self, nums: List[int], k: int) -> int:
        ans = [-float('inf') for _ in range(len(nums))]
        ans[0] = nums[0]
        for i in range(1, len(nums)):
            start = i - k if i - k >= 0 else 0
            ans[i] = max(ans[start:i]) + nums[i]

        return ans[-1]


class Solution3:
    """priority queue"""
    def maxResult(self, nums: List[int], k: int) -> int:
        ans = nums[0]
        q = [[-nums[0], 0]]
        for i in range(1, len(nums)):
            while q and q[0][1] < i - k:
                heapq.heappop(q)
            ans = nums[i] + q[0][0] * -1
            heapq.heappush(q, [-ans, i])
        return ans
