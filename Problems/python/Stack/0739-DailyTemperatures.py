"""
Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.



Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]


Constraints:

1 <= temperatures.length <= 10^5
30 <= temperatures[i] <= 100
"""
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(-float('inf'), 0)]
        ans = []

        for i, t in enumerate(temperatures[::-1]):
            while stack and stack[-1][0] <= t:
                stack.pop()
            if stack:
                ans.append(i - stack[-1][1])
            else:
                ans.append(0)
            stack.append((t, i))
        return ans[::-1]


class Solution2:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0 for _ in range(len(temperatures))]
        stack = []
        for i, t in enumerate(temperatures):
            while stack and stack[-1][0] < t:
                pre_t, pre_i = stack.pop()
                ans[pre_i] = i - pre_i
            stack.append((t, i))
        return ans
