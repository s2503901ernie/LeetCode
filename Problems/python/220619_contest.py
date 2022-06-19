class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        return self.dfs(s, k, 0)

    def dfs(self, s, k, ans):
        if not s:
            return 0
        if int(s, 2) <= k:
            return len(s)
        for i in range(len(s)):
            ans = max(self.dfs(s[:i] + s[i+1:], k, ans), ans)

        return ans
