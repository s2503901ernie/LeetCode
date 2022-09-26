"""
You are given an array of strings equations that represent relationships between variables where each string equations[i] is of length 4 and takes one of two different forms: "xi==yi" or "xi!=yi".Here, xi and yi are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if it is possible to assign integers to variable names so as to satisfy all the given equations, or false otherwise.



Example 1:

Input: equations = ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.
There is no way to assign the variables to satisfy both equations.
Example 2:

Input: equations = ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.


Constraints:

1 <= equations.length <= 500
equations[i].length == 4
equations[i][0] is a lowercase letter.
equations[i][1] is either '=' or '!'.
equations[i][2] is '='.
equations[i][3] is a lowercase letter.
"""
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        d = {}
        for e in equations:
            if e[1:3] == '!=':
                continue
            x, y = e.split('==')
            self.merge(x, y, d)
        for e in equations:
            if e[1:3] == '==':
                continue
            x, y = e.split('!=')
            if self.find(x, d) == self.find(y, d):
                return False

        return True

    def find(self, x, d):
        if x not in d:
            return x
        if x == d[x]:
            return x
        return self.find(d[x], d)

    def merge(self, x, y, d):
        p_x = self.find(x, d)
        p_y = self.find(y, d)
        if p_x != p_y:
            d[p_y] = p_x
