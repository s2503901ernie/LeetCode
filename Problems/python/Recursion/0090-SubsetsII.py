"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.



Example 1:

Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:

Input: nums = [0]
Output: [[],[0]]


Constraints:

1 <= nums.length <= 10
-10 <= nums[i] <= 10
"""
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[], nums]
        nums.sort()
        ans = [[]]
        for ele in nums:
            for i in range(len(ans)):
                new = ans[i] + [ele]
                if new not in ans:
                    ans.append(new)

        return ans


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        nums.sort()
        ans = [[]]
        cur = []
        for i in range(len(nums)):
            new_cur = []
            if i > 0 and nums[i] == nums[i-1]:
                for c in cur:
                    new_cur.append(c + [nums[i]])
            else:
                n = len(ans)
                for j in range(n):
                    new_cur.append(ans[j] + [nums[i]])
            ans += new_cur
            cur = new_cur

        return ans
