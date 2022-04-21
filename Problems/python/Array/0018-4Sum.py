"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.



Example 1:

Input: nums = [1,0,-1,0,-2,2], target = 0
Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

Example 2:

Input: nums = [2,2,2,2,2], target = 8
Output: [[2,2,2,2]]


Constraints:

1 <= nums.length <= 200
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9
"""
from typing import List


class Solution1:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            diff = target - nums[i]
            three_sum_results = self.threeSum(nums[i+1:], diff)
            for three_sum_result in three_sum_results:
                results.append([nums[i]] + three_sum_result)

        return results

    def threeSum(self, nums, target) -> List[List[int]]:
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            diff = target - nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current = nums[left] + nums[right]
                if current == diff:
                    results.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif current < diff:
                    left += 1
                else:
                    right -= 1

        return results


class Solution2:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        pairs = {}
        results = []
        nums.sort()
        for i in range(2, len(nums) - 1):
            for k in range(i-1):
                if k > 0 and nums[k] == nums[k-1]:
                    continue
                current = nums[k] + nums[i-1]
                pair = [nums[k], nums[i-1]]
                if current not in pairs:
                    pairs[current] = [pair]
                else:
                    pairs[current].append(pair)

            for j in range(i+1, len(nums)):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                current = nums[j] + nums[i]
                diff = target - current
                if diff in pairs:
                    for pair in pairs[diff]:
                        added = [nums[j], nums[i]] + pair
                        if added not in results:
                            results.append([nums[j], nums[i]] + pair)

        return results
