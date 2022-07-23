"""
You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].



Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]


Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4
"""
from typing import List


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        self.res = [0 for _ in range(len(nums))]
        rank = [(i, n) for i, n in enumerate(nums)]
        self.divide(rank)

        return self.res

    def divide(self, rank):
        if len(rank) < 2:
            return rank
        mid = len(rank) // 2
        left = self.divide(rank[:mid])
        right = self.divide(rank[mid:])

        return self.merge(left, right)

    def merge(self, left, right):
        i, j = 0, 0
        arr = []
        while i < len(left) and j < len(right):
            if left[i][1] > right[j][1]:
                arr.append(left[i])
                self.res[left[i][0]] += len(right) - j
                i += 1
            else:
                arr.append(right[j])
                j += 1
        arr.extend(left[i:]) if left[i:] else arr.extend(right[j:])

        return arr
