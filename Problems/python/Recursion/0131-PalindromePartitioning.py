"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.



Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]


Constraints:

1 <= s.length <= 16
s contains only lowercase English letters.
"""


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.helper(s, [], ans)

        return ans

    def helper(self, string, current, ans):
        if not string:
            ans.append(current)
            return
        for i in range(len(string)):
            if self.ispalindrome(string[:i+1]) is True:
                new_current = current + [string[:i+1]]
                self.helper(string[i+1:], new_current, ans)

    def ispalindrome(self, string):
        left = 0
        right = len(string) - 1
        while left <= right:
            if string[left] != string[right]:
                return False
            left += 1
            right -= 1

        return True
