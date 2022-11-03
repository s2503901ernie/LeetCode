# You are given an array of strings words. Each element of words consists of
# two lowercase English letters.
#
#  Create the longest possible palindrome by selecting some elements from words
# and concatenating them in any order. Each element can be selected at most once.
#
#
#  Return the length of the longest palindrome that you can create. If it is
# impossible to create any palindrome, return 0.
#
#  A palindrome is a string that reads the same forward and backward.
#
#
#  Example 1:
#
#
# Input: words = ["lc","cl","gg"]
# Output: 6
# Explanation: One longest palindrome is "lc" + "gg" + "cl" = "lcggcl", of
# length 6.
# Note that "clgglc" is another longest palindrome that can be created.
#
#
#  Example 2:
#
#
# Input: words = ["ab","ty","yt","lc","cl","ab"]
# Output: 8
# Explanation: One longest palindrome is "ty" + "lc" + "cl" + "yt" = "tylcclyt",
#  of length 8.
# Note that "lcyttycl" is another longest palindrome that can be created.
#
#
#  Example 3:
#
#
# Input: words = ["cc","ll","xx"]
# Output: 2
# Explanation: One longest palindrome is "cc", of length 2.
# Note that "ll" is another longest palindrome that can be created, and so is
# "xx".
#
#
#
#  Constraints:
#
#
#  1 <= words.length <= 10⁵
#  words[i].length == 2
#  words[i] consists of lowercase English letters.
#
#
#  Related Topics Array Hash Table String Greedy Counting 👍 1495 👎 29
from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        ans = 0
        for w in words:
            d[w] = d.get(w, 0) + 1
        for w in words:
            if w == w[::-1]:
                if d[w] > 1:
                    ans += 4
                    d[w] -= 2
            else:
                if d[w] > 0 and d.get(w[::-1], 0) > 0:
                    ans += 4
                    d[w] -= 1
                    d[w[::-1]] -= 1
        for k, v in d.items():
            if k == k[::-1] and v > 0:
                return ans + 2
        return ans
