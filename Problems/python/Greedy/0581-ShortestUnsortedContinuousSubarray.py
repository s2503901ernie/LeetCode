"""
Given an integer array nums, you need to find one continuous subarray that if you only sort this subarray in ascending order, then the whole array will be sorted in ascending order.

Return the shortest such subarray and output its length.



Example 1:

Input: nums = [2,6,4,8,10,9,15]
Output: 5
Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array sorted in ascending order.
Example 2:

Input: nums = [1,2,3,4]
Output: 0
Example 3:

Input: nums = [1]
Output: 0


Constraints:

1 <= nums.length <= 10^4
-10^5 <= nums[i] <= 10^5
"""
from typing import List


class Solution1:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        compared = sorted(nums)
        left = len(nums)
        right = 0
        for i in range(len(nums)):
            if nums[i] != compared[i]:
                left = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != compared[i]:
                right = i
                break

        if left > right:
            return 0
        return right - left + 1


class Solution2:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        end = 0
        prev = nums[0]
        for i in range(1, len(nums)):
            if nums[i] < prev:
                end = i
            else:
                prev = nums[i]
        start = len(nums) - 1
        prev = nums[start]
        for i in range(len(nums) - 2, -1, -1):
            if nums[i] > prev:
                start = i
            else:
                prev = nums[i]
        if end == 0:
            return 0
        return end - start + 1


class Solution3:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0
        left = len(nums)
        for i in range(len(nums) - 1):
            if nums[i] > nums[i+1]:
                left = i
                break
        if left == len(nums):
            return 0
        right = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i-1] > nums[i]:
                right = i
                break

        tmp = nums[left:right+1]
        min_val = min(tmp)
        max_val = max(tmp)
        i = left
        while i > 0:
            if nums[i] > min_val:
                left = i
            i -= 1
        i = right
        while i < len(nums):
            if nums[i] < max_val:
                right = i
            i += 1

        return right - left + 1



