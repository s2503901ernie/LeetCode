"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        candidates.sort()
        self.helper(candidates, [], target, ans)

        return ans

    def helper(self, candidates, current, target, ans):
        if target == 0:
            ans.append(current)
            return

        for i in range(len(candidates)):
            if target - candidates[i] < 0:
                break
            if i > 0 and candidates[i] == candidates[i-1]:
                continue
            new_target = target - candidates[i]
            new_current = current + [candidates[i]]
            new_candidates = candidates[i+1:]
            self.helper(new_candidates, new_current, new_target, ans)
