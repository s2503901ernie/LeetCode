"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.



Example 1:

Input: nums = [3,2,3]
Output: [3]
Example 2:

Input: nums = [1]
Output: [1]
Example 3:

Input: nums = [1,2]
Output: [1,2]


Constraints:

1 <= nums.length <= 5 * 10^4
-10^9 <= nums[i] <= 10^9
"""


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return [nums[0]]
        nums.sort()
        limit = len(nums) / 3.0
        count = 0
        ans = set()
        for i in range(len(nums)):
            if i == 0:
                count = 1
                if count > limit:
                    ans.add(nums[0])
                continue
            if nums[i] == nums[i - 1]:
                count += 1
                if nums[i] in ans:
                    continue
                if count > limit:
                    ans.add(nums[i])
            else:
                count = 1
                if count > limit:
                    ans.add(nums[i])

        return list(ans)
