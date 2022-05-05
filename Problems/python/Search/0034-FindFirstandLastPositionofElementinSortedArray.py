"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
nums is a non-decreasing array.
-10^9 <= target <= 10^9
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        ans = []
        ans.append(self.helper_left(nums, target, left, right))
        ans.append(self.helper_right(nums, target, left, right))

        return ans

    def helper_left(self, nums, target, left, right):
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                right = mid - 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return res

    def helper_right(self, nums, target, left, right):
        res = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                res = mid
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return res


class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = []
        left = 0
        right = len(nums) - 1
        ans.append(self.helper(nums, target, left, right))
        ans.append(self.helper(nums, target + 1, left, right) - 1)
        if ans[0] > ans[1]:
            return [-1, -1]

        return ans

    def helper(self, nums, target, left, right):
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid - 1
            else:
                left = mid + 1

        return left
