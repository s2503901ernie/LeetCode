from collections import defaultdict


class Solution:
    def numberOfSubarrays(self, nums: List[int]) -> int:
        ans = [[0, 0] for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                ans[i][0] = 1
                ans[i][1] = i
                continue
            if nums[i] < nums[i + 1]:
                ans[i][0] = 1
                ans[i][1] = i
                continue
            if nums[i] == nums[i + 1]:
                ans[i][0] = ans[i + 1][0] + 1
                ans[i][1] = ans[i + 1][1]
                continue
            count, stop = self.dfs(ans[i + 1][1], nums, nums[i])
            ans[i][0] = count + 1
            ans[i][1] = stop
        counts = 0
        for c, _ in ans:
            counts += c
        return counts

    def dfs(self, start, nums, max_val):
        cur = 0
        stop = len(nums) - 1
        for i in range(start, len(nums)):
            if nums[i] == max_val:
                cur += 1
            if nums[i] > max_val:
                stop = i
                break
        return cur, stop

