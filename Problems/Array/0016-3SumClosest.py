"""
Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.



Example 1:

Input: nums = [-1,2,1,-4], target = 1
Output: 2
Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
Example 2:

Input: nums = [0,0,0], target = 1
Output: 0


Constraints:

3 <= nums.length <= 1000
-1000 <= nums[i] <= 1000
-10^4 <= target <= 10^4
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        min_value = float("inf")
        board = {}
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] in board:
                continue
            else:
                board[nums[i]] = True
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[i] + nums[left] + nums[right]
                if abs(current - target) < min_value:
                    ans = current
                    min_value = abs(current - target)
                if current < target:
                    left += 1
                elif current > target:
                    right -= 1
                else:
                    return target

        return ans