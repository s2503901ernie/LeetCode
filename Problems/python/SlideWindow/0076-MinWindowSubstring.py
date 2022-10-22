# Given two strings s and t of lengths m and n respectively, return the minimum
# window substring of s such that every character in t (including duplicates) is
# included in the window. If there is no such substring, return the empty string
# "".
#
#  The testcases will be generated such that the answer is unique.
#
#  A substring is a contiguous sequence of characters within the string.
#
#
#  Example 1:
#
#
# Input: s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"
# Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C'
# from string t.
#
#
#  Example 2:
#
#
# Input: s = "a", t = "a"
# Output: "a"
# Explanation: The entire string s is the minimum window.
#
#
#  Example 3:
#
#
# Input: s = "a", t = "aa"
# Output: ""
# Explanation: Both 'a's from t must be included in the window.
# Since the largest window of s only has one 'a', return empty string.
#
#
#
#  Constraints:
#
#
#  m == s.length
#  n == t.length
#  1 <= m, n <= 10⁵
#  s and t consist of uppercase and lowercase English letters.
#
#
#
#  Follow up: Could you find an algorithm that runs in O(m + n) time?
#
#  Related Topics Hash Table String Sliding Window 👍 12736 👎 579


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m, n = len(s), len(t)
        if m < n:
            return ""
        d = {}
        for c in t:
            d[c] = d.get(c, 0) + 1
        start, end = 0, float('inf')
        i = 0
        for j, c in enumerate(s):
            if c not in d:
                continue
            if d[c] > 0:
                n -= 1
            d[c] -= 1
            if n == 0:
                while i < j:
                    if s[i] in d and d[s[i]] == 0:
                        d[s[i]] += 1
                        break
                    if s[i] in d:
                        d[s[i]] += 1
                    i += 1
                n += 1
                if j - i < end - start:
                    start, end = i, j
                i += 1
        if end == float('inf'):
            return ""
        return s[start:end + 1]
