"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.



Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true

Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true

Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false


Constraints:

1 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9
0 <= k <= 10^5
"""
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        board = {}
        for i in range(len(nums)):
            if nums[i] in board:
                if i - board[nums[i]][-1] <= k:
                    return True
                board[nums[i]].append(i)
            else:
                board[nums[i]] = [i]

        return False
