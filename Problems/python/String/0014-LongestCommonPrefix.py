"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.


Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lower-case English letters.
"""
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common = strs[0]

        for string in strs[1:]:
            n = 0
            while n < len(common) and n < len(string):
                if common[n] == string[n]:
                    n += 1
                else:
                    break
            common = common[:n]
            if len(common) == 0:
                return ""

        return common
