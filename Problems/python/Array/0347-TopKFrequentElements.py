"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.



Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:

Input: nums = [1], k = 1
Output: [1]


Constraints:

1 <= nums.length <= 10^5
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
"""
import heapq
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        board = {}
        ans = []
        for num in nums:
            if num not in board:
                board[num] = 1
            else:
                board[num] += 1
        for i in range(k):
            ans.append(max(board, key=board.get))
            board.pop(ans[-1])

        return ans


class Solution2:
    """bucket"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        board = {}
        ans = []
        for num in nums:
            board[num] = board.setdefault(num, 0) + 1
        buckets = [[]for _ in range(len(nums)+1)]
        for key, freq in board.items():
            buckets[freq].append(key)
        for i in range(len(buckets)-1, -1, -1):
            bucket = buckets[i]
            if bucket:
                for num in bucket:
                    ans.append(num)
            if len(ans) == k:
                break

        return ans


class Solution3:
    """heap"""
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for n in nums:
            d[n] = d.get(n, 0) - 1
        stack = []
        ans = []
        for n, f in d.items():
            heapq.heappush(stack, [f, n])
        for _ in range(k):
            ans.append(heapq.heappop(stack)[1])

        return ans
