"""
You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).



Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.


Constraints:

1 <= nums.length <= 10^4
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.
"""
from collections import defaultdict
import heapq
from typing import List


class Solution:
    """heap"""
    def isPossible(self, nums: List[int]) -> bool:
        q = [[]]

        for num in nums:
            stack = []
            while q:
                cur = heapq.heappop(q)
                if not cur or -cur[0] == num - 1:
                    cur.insert(0, -num)
                    heapq.heappush(q, cur)
                    break
                else:
                    if -cur[0] < num - 1 and len(cur) < 3:
                        return False
                    heapq.heappush(stack, cur)
            if not q:
                heapq.heappush(stack, [-num])
                q = stack
            else:
                while stack:
                    heapq.heappush(q, stack.pop())
        for s in q:
            if len(s) < 3:
                return False
        return True


class Solution2:
    """Greedy"""
    def isPossible(self, nums: List[int]) -> bool:
        used = {}
        seq = defaultdict(int)
        for num in nums:
            used[num] = used.get(num, 0) + 1
        for num in nums:
            if used[num] == 0:
                continue
            if seq[num - 1] > 0:
                seq[num - 1] -= 1
                seq[num] += 1
            else:
                if used.get(num + 1, 0) < 1 or used.get(num + 2, 0) < 1:
                    return False
                seq[num + 2] += 1
                used[num + 1] -= 1
                used[num + 2] -= 1
            used[num] -= 1

        return True
