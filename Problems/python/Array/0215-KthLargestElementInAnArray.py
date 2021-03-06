"""
Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.



Example 1:

Input: nums = [3,2,1,5,6,4], k = 2
Output: 5

Example 2:

Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
Output: 4


Constraints:

1 <= k <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
"""
import time
from random import randint
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()

        return nums[-k]


class Solution2:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        length = len(nums)
        left = 0
        right = length - 1
        while True:
            pos = self.partition(nums, left, right)
            if pos + k == length:
                return nums[pos]
            elif pos + k > length:
                left = 0
                right = pos - 1
            else:
                left = pos + 1

    def partition(self, nums, left, right) -> int:
        idx = left
        while left < right:
            if nums[left] < nums[right]:
                nums[idx], nums[left] = nums[left], nums[idx]
                idx += 1
            left += 1

        nums[idx], nums[right] = nums[right], nums[idx]

        return idx


class Solution3:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            for j in range(len(nums) - i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]

        return nums[-k]


def main():
    start1 = time.perf_counter()
    nums1 = [randint(1, 20000) for _ in range(30000)]
    nums2 = nums1.copy()
    k = 10000
    sol2 = Solution2()
    ans = sol2.findKthLargest(nums1, k)
    end1 = time.perf_counter()
    start2 = time.perf_counter()
    nums2.sort()
    end2 = time.perf_counter()
    print(ans, nums2[-k])
    print(f'quick select spends: {end1 - start1:0.8f}, '
          f'sort solution spends: {end2 - start2:0.8f}')


if __name__ == '__main__':
    main()
