class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97}
        min_idx = float('inf')
        max_idx = -float('inf')
        for i, num in enumerate(nums):
            if num not in primes:
                continue
            min_idx = min(min_idx, i)
            max_idx = max(max_idx, i)
        return max_idx - min_idx

