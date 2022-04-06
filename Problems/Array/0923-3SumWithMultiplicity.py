"""
Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.



Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation:
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation:
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.


Constraints:

3 <= arr.length <= 3000
0 <= arr[i] <= 100
0 <= target <= 300
"""
from typing import List


class Solution1:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        arr.sort()
        board = {}
        ans = 0
        for num in arr:
            board[num] = board.get(num, 0) + 1
        i = 0
        length = len(arr)
        while i < length:
            num_i = board[arr[i]]
            left = i
            right = length - 1
            while left < right:
                current = arr[i] + arr[left] + arr[right]
                num_left = board[arr[left]]
                num_right = board[arr[right]]
                if current > target:
                    right -= num_right
                elif current < target:
                    left += num_left
                else:
                    if arr[i] != arr[left] != arr[right]:
                        ans += num_i * num_left * num_right
                    elif arr[i] == arr[left] != arr[right]:
                        ans += num_i * (num_left - 1) // 2 * num_right
                    elif arr[i] != arr[left] == arr[right]:
                        ans += num_i * num_left * (num_right - 1) // 2
                    else:
                        ans += num_i * (num_left - 2) * (num_right - 1) // 6
                    left += num_left
                    right -= num_right

            i += num_i

        return ans % (10 ** 9 + 7)
