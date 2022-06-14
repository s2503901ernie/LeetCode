"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.



Example 1:

Input: word1 = "sea", word2 = "eat"
Output: 2
Explanation: You need one step to make "sea" to "ea" and another step to make "eat" to "ea".
Example 2:

Input: word1 = "leetcode", word2 = "etco"
Output: 4


Constraints:

1 <= word1.length, word2.length <= 500
word1 and word2 consist of only lowercase English letters.
"""


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        ans = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            ans[i][0] = i
        for j in range(1, len(word2) + 1):
            ans[0][j] = j

        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if word1[i - 1] == word2[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1]
                else:
                    ans[i][j]= 1 + min(ans[i - 1][j], ans[i][j - 1])

        return ans[-1][-1]


class Solution2:
    """Find the longest common substring."""
    def minDistance(self, word1: str, word2: str) -> int:
        ans = [[0 for _ in range(len(word2) + 1)] for _ in range(len(word1) + 1)]
        for i in range(1, len(word1) + 1):
            for j in range(1, len(word2) + 1):
                if ans[i - 1] == ans[j - 1]:
                    ans[i][j] = ans[i - 1][j - 1] + 1
                else:
                    ans[i][j] = max(ans[i - 1][j], ans[i][j - 1])

        return len(word1) - ans[-1][-1] + len(word2) - ans[-1][-1]
