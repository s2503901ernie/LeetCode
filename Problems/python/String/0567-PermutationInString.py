"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.



Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false


Constraints:

1 <= s1.length, s2.length <= 10^4
s1 and s2 consist of lowercase English letters.
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        board_s1 = {}
        board_s2 = {}
        for letter in s1:
            if letter not in board_s1:
                board_s1[letter] = 1
            else:
                board_s1[letter] += 1
        for i in range(len(s1) - 1):
            if s2[i] not in board_s2:
                board_s2[s2[i]] = 1
            else:
                board_s2[s2[i]] += 1
        for i in range(len(s1) - 1, len(s2)):
            if s2[i] not in board_s2:
                board_s2[s2[i]] = 1
            else:
                board_s2[s2[i]] += 1
            if board_s1 == board_s2:
                return True
            board_s2[s2[i - len(s1) + 1]] -= 1
            if board_s2[s2[i - len(s1) + 1]] == 0:
                board_s2.pop(s2[i - len(s1) + 1])

        return False
