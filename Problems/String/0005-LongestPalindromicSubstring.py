"""
Given a string s, return the longest palindromic substring in s.



Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"


Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0, 0]
        # odd
        for i in range(len(s)):
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left > ans[1] - ans[0]:
                        ans = [left, right]
                    left -= 1
                    right += 1
                else:
                    break
        # even
        for i in range(len(s)):
            left = i
            right = i + 1
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    if right - left > ans[1] - ans[0]:
                        ans = [left, right]
                    left -= 1
                    right += 1
                else:
                    break

        return s[ans[0]: ans[1] + 1]
