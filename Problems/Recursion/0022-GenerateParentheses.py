"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.



Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:

Input: n = 1
Output: ["()"]


Constraints:

1 <= n <= 8
"""
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.helper(0, 0, "", n, ans)

        return ans

    def helper(self, left, right, current, n, ans):
        if left < right:
            return
        if left == n and right == n:
            ans.append(current)
            return
        if left > n or right > n:
            return
        new_current = current + "("
        self.helper(left + 1, right, new_current, n, ans)
        new_current = current + ")"
        self.helper(left, right + 1, new_current, n, ans)
