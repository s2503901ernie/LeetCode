"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.



Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".


Constraints:

1 <= s.length, p.length <= 3 * 10^4
s and p consist of lowercase English letters.
"""
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        ans = []
        ana_s = {}
        ana_p = {}
        for letter in p:
            if letter not in ana_p:
                ana_p[letter] = 1
            else:
                ana_p[letter] += 1
        for i in range(len(p) - 1):
            if s[i] not in ana_s:
                ana_s[s[i]] = 1
            else:
                ana_s[s[i]] += 1
        for i in range(len(p) - 1, len(s)):
            if s[i] not in ana_s:
                ana_s[s[i]] = 1
            else:
                ana_s[s[i]] += 1
            if ana_s == ana_p:
                ans.append(i - len(p) + 1)
            ana_s[s[i - len(p) + 1]] -= 1
            if ana_s[s[i - len(p) + 1]] == 0:
                ana_s.pop(s[i - len(p) + 1])

        return ans
