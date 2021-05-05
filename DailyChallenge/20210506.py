class Solution:
    def jump(self, nums: List[int]) -> int:
        n = 0
        i = 0
        while i < len(nums) - 1:
            step = nums[i]
            n += 1
            if i + step >= len(nums) - 1:
                break
            i += 1
            max_distance = i + nums[i]
            for j in range(i+1, i+step):
                if j + nums[j] >= max_distance:
                    i = j
                    max_distance = j + nums[j]

        return n
