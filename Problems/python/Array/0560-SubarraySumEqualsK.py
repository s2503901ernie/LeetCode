"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2


Constraints:

1 <= nums.length <= 2 * 10^4
-1000 <= nums[i] <= 1000
-10^7 <= k <= 10^7
"""
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = {0: 1}
        cur = 0
        ans = 0
        for num in nums:
            cur += num
            if cur - k in d:
                ans += d[cur - k]
            if cur in d:
                d[cur] += 1
            else:
                d[cur] = 1

        return ans
