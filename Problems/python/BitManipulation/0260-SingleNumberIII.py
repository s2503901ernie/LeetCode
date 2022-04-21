"""
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.



Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.

Example 2:

Input: nums = [-1,0]
Output: [-1,0]

Example 3:

Input: nums = [0,1]
Output: [1,0]


Constraints:

2 <= nums.length <= 3 * 10^4
-2^31 <= nums[i] <= 2^31 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        ans1 = 0
        ans2 = 0
        bit = 0
        for num in nums:
            ans1 ^= num
        for i in range(32):
            if ans1 & 1 << i != 0:
                bit = i
                break
        for num in nums:
            if num & 1 << bit != 0:
                ans2 ^= num

        return [ans1 ^ ans2, ans2]
