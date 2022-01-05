"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.



Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]
Example 2:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]


Constraints:

1 <= nums.length <= 8
-10 <= nums[i] <= 10
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.helper(nums, [], ans)

        return ans

    def helper(self, array: list, current: list, ans: list):
        if not array:
            ans.append(current)
            return
        board = {}
        for i in range(len(array)):
            if array[i] not in board:
                board[array[i]] = True
            else:
                continue
            new_current = current + [array[i]]
            new_array = array[:i] + array[i+1:]
            self.helper(new_array, new_current, ans)
