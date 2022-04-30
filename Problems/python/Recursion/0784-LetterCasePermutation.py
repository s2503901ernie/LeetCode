"""
Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.



Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]


Constraints:

1 <= s.length <= 12
s consists of lowercase English letters, uppercase English letters, and digits.
"""
from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = []
        self.helper(s, [], ans)

        return ans

    def helper(self, string: str, cur, ans):
        if not string:
            ans.append("".join(cur))
            return

        s = string[0]
        if s.isalpha() is True:
            cur1 = cur + [s.lower()]
            cur2 = cur + [s.upper()]
            self.helper(string[1:], cur1, ans)
            self.helper(string[1:], cur2, ans)
        else:
            cur3 = cur + [s]
            self.helper(string[1:], cur3, ans)
