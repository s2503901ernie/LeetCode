"""
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.



Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.


Constraints:

1 <= intervals.length <= 10^5
intervals[i].length == 2
-5 * 10^4 <= starti < endi <= 5 * 10^4
"""
from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        nums = sorted(intervals, key=lambda x: x[0])
        end = nums[0][1]
        for num in nums[1:]:
            if num[0] >= end:
                end = num[1]
            else:
                ans += 1
                if num[1] < end:
                    end = num[1]

        return ans


class Solution2:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ans = 0
        nums = sorted(intervals, key=lambda x: x[1])
        end = nums[0][1]
        for num in nums[1:]:
            if num[0] >= end:
                end = num[1]
            else:
                ans += 1

        return ans

        


