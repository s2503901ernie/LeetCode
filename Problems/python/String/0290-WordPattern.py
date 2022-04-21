"""
Given a pattern and a string s, find if s follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.



Example 1:

Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:

Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:

Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false


Constraints:

1 <= pattern.length <= 300
pattern contains only lower-case English letters.
1 <= s.length <= 3000
s contains only lowercase English letters and spaces ' '.
s does not contain any leading or trailing spaces.
All the words in s are separated by a single space.
"""


class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        board_s = {}
        board_pattern = {}
        s = str.split()
        if len(pattern) != len(s):

            return False

        for i in range(len(pattern)):
            if s[i] not in board_s:
                board_s[s[i]] = [i]
                if pattern[i] in board_pattern:

                    return False

                else:
                    board_pattern[pattern[i]] = [i]
            else:
                board_s[s[i]].append(i)
                if pattern[i] not in board_pattern:

                    return False

                else:
                    board_pattern[pattern[i]].append(i)
                    if board_s[s[i]] != board_pattern[pattern[i]]:

                        return False

        return True
