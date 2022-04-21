"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.



Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:

Input: nums = []
Output: []

Example 3:

Input: nums = [0]
Output: []


Constraints:

0 <= nums.length <= 3000
-10^5 <= nums[i] <= 10^5
"""


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        board = {}
        ans = []
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] not in board:
                board[nums[i]] = True
            else:
                continue
            target = 0 - nums[i]
            left = i + 1
            right = len(nums) - 1
            tmp_board = {}
            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    if nums[left] not in tmp_board and nums[right] not in tmp_board:
                        ans.append([nums[i], nums[left], nums[right]])
                        tmp_board[nums[left]] = True
                        tmp_board[nums[right]] = True
                    left += 1
                    right -= 1

        return ans
