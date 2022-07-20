"""
Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".


Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".
Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2


Constraints:

1 <= s.length <= 5 * 10^4
1 <= words.length <= 5000
1 <= words[i].length <= 50
s and words[i] consist of only lowercase English letters.
"""
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        d = {}
        ans = 0
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = [i]
            else:
                d[s[i]].append(i)

        for word in words:
            tmp = {}
            p = 0
            cur = 0
            for w in word:
                if w not in d:
                    break
                start = tmp.get(w, 0)
                for i in range(start, len(d[w])):
                    if p <= d[w][i]:
                        tmp[w] = i + 1
                        p = d[w][i]
                        cur += 1
                        break

            if cur == len(word):
                ans += 1

        return ans
