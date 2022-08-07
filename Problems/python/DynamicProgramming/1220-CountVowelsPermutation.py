"""
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:

Each character is a lower case vowel ('a', 'e', 'i', 'o', 'u')
Each vowel 'a' may only be followed by an 'e'.
Each vowel 'e' may only be followed by an 'a' or an 'i'.
Each vowel 'i' may not be followed by another 'i'.
Each vowel 'o' may only be followed by an 'i' or a 'u'.
Each vowel 'u' may only be followed by an 'a'.
Since the answer may be too large, return it modulo 10^9 + 7.



Example 1:

Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".
Example 2:

Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".
Example 3:

Input: n = 5
Output: 68


Constraints:

1 <= n <= 2 * 10^4
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        d = {"a": 1, "e": 1, "i": 1, "o": 1, "u": 1}
        ans = 5
        for i in range(1, n):
            ans = 0
            tmp = {"a": 0, "e": 0, "i": 0, "o": 0, "u": 0}
            tmp["a"] = tmp["a"] + d.get("e") + d.get("i") + d.get("u")
            tmp["e"] = tmp["e"] + d.get("a") + d.get("i")
            tmp["i"] = tmp["i"] + d.get("e") + d.get("o")
            tmp["o"] = tmp["o"] + d.get("i")
            tmp["u"] = tmp["u"] + d.get("i") + d.get("o")
            ans += tmp["a"] + tmp["e"] + tmp["i"] + tmp["o"] + tmp["u"]
            d = tmp
        return ans % (10 ** 9 + 7)


class Solution2:
    def countVowelPermutation(self, n: int) -> int:
        a, e, i, o, u = 1, 1, 1, 1, 1
        for _ in range(n - 1):
            a, e, i, o, u = e + i + u, a + i, e + o, i, i + o

        return (a + e + i + o + u) / (10 ** 9 + 7)
