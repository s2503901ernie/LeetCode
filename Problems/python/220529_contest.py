class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        cur = nums[0]
        stack = []
        ans = 0
        tmp = 0
        for i in range(1, len(nums)):
            if not stack and nums[i] < cur:
                stack.append(nums[i])
                tmp += 1
            elif stack and stack[-1] <= nums[i] and nums[i] < cur:

                tmp += 1
                stack.append(nums[i])
            else:
                ans = max(ans, tmp)
                tmp = 0
                cur = nums[i]
                stack = []
        ans = max(ans, tmp)

        return ans

