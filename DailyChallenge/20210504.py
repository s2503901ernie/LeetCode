class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) == 1 or len(nums) == 2:
            return True
        if nums[1] < nums[0]:
            n = 1
            nums[0] = nums[1]
        else:
            n = 0
        for i in range(2, len(nums)):
            if nums[i] < nums[i-1]:
                n += 1
                if nums[i] < nums[i-2]:
                    nums[i] = nums[i-1]
                else:
                    nums[i-1] = nums[i]
            if n > 1:
                return False
        return True
