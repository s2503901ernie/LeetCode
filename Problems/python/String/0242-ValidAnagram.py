"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.


Example 1:

Input: s = "anagram", t = "nagaram"
Output: true

Example 2:

Input: s = "rat", t = "car"
Output: false


Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))

        return s == t
