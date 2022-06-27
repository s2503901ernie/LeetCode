"""
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.



Example 1:

Input: s = "tree"
Output: "eert"
Explanation: 'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.
Example 2:

Input: s = "cccaaa"
Output: "aaaccc"
Explanation: Both 'c' and 'a' appear three times, so both "cccaaa" and "aaaccc" are valid answers.
Note that "cacaca" is incorrect, as the same characters must be together.
Example 3:

Input: s = "Aabb"
Output: "bbAa"
Explanation: "bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.


Constraints:

1 <= s.length <= 5 * 10^5
s consists of uppercase and lowercase English letters and digits.
"""
import heapq


class Solution:
    """heap"""
    def frequencySort(self, s: str) -> str:
        d = {}
        stack = []
        ans = []
        for i in s:
            d[i] = d.get(i, 0) - 1
        for k, v in d.items():
            heapq.heappush(stack, [v, k])
        for _ in range(len(stack)):
            cur = heapq.heappop(stack)
            ans.append(-cur[0] * cur[1])

        return "".join(ans)


class Solution2:
    """bucket select"""
    def frequencySort(self, s: str) -> str:
        d = {}
        ans = []
        b = [[] for _ in range(len(s))]
        for i in s:
            d[i] = d.get(i, 0) + 1
        for k, v in d.items():
            b[v].append(k)
        for i in range(len(s) - 1, -1, -1 ):
            if not b[i]:
                continue
            for c in b[i]:
                ans.append(i * c)

        return "".join(ans)
