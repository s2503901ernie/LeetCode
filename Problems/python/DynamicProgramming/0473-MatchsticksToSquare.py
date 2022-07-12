"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.



Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.


Constraints:

1 <= matchsticks.length <= 15
1 <= matchsticks[i] <= 10^8
"""
from typing import List


class Solution:
    """TLE"""
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        l = sum(matchsticks) / 4
        matchsticks.sort(reverse=True)

        return self.dfs(matchsticks, l, 0, 4)

    def dfs(self, m, l, cur, remain):
        if not m and remain == 0:
            return True
        for i in range(len(m)):
            if m[i] + cur == l:
                remain -= 1
                cur = 0
                return self.dfs(m[:i] + m[i+1:], l, cur, remain)
            elif m[i] + cur < l:
                cur = cur + m[i]
                return self.dfs(m[:i] + m[i+1:], l, cur, remain)
            else:
                return False


class Solution2:
    def makesquare(self, nums: List[int]) -> bool:
        nums.sort(reverse=True)
        if len(nums) < 4:
            return False
        total = sum(nums)
        if total % 4 != 0:
            return False
        target = total / 4
        if any(n > target for n in nums):
            return False
        return self.dfs([target] * 4, 0, nums)

    def dfs(self, lefts, idx, nums):
        if idx == len(nums):
            return True
        n = nums[idx]
        used = set()
        for i, left in enumerate(lefts):
            if left >= n and left not in used:
                lefts[i] -= n
                if self.dfs(lefts, idx + 1, nums):
                    return True
                lefts[i] += n
                used.add(left)
        return False
