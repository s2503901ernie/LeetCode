"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.



Example 1:

Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:

Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.


Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 != 0:
            return False
        dp = [False for _ in range(sum(nums) // 2 + 1)]
        dp[0] = True
        for num in nums:
            for target in range(sum(nums) // 2, num - 1, -1):
                dp[target] = dp[target] or dp[target - num]
            if dp[-1] is True:
                return True

        return False
