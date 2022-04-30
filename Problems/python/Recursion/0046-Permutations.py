"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]

Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]

Example 3:

Input: nums = [1]
Output: [[1]]


Constraints:

1 <= nums.length <= 6
-10 <= nums[i] <= 10
All the integers of nums are unique.
"""
from typing import List


class Solution:
    """ DFS """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)

        return ans

    def helper(self, array, current, ans):
        if not array:
            ans.append(current)
            return
        for i in range(len(array)):
            new_array = array[:i] + array[i+1:]
            new_current = current + [array[i]]
            self.helper(new_array, new_current, ans)


class Solution2:
    """ DFS slightly improvement """
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)

        return ans

    def helper(self, nums, arr, ans):
        if not nums:
            ans.append(arr)
            return
        for i in range(len(nums)):
            new_arr = arr + [nums[i]]
            self.helper(nums[:i] + nums[i+1:], new_arr, ans)
