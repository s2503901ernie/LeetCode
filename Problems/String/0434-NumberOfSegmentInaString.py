"""
Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.



Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]

Example 2:

Input: s = "Hello"
Output: 1


Constraints:

0 <= s.length <= 300
s consists of lowercase and uppercase English letters, digits, or one of the following characters "!@#$%^&*()_+-=',.:".
The only space character in s is ' '.
"""


class Solution:
    def countSegments(self, s: str) -> int:
        ans = 0
        cur = False
        for i in s:
            if i != " " and cur is False:
                ans += 1
                cur = True
            elif i == " ":
                cur = False

        return ans
