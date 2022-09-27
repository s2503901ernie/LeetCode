"""
There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.



Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."


Constraints:

n == dominoes.length
1 <= n <= 10^5
dominoes[i] is either 'L', 'R', or '.'.
"""


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        if len(dominoes) == 1:
            return dominoes
        c = True
        dominoes = list(dominoes)
        while c:
            c = False
            tmp = dominoes.copy()
            for i, d in enumerate(dominoes):
                if d == 'L' or d == 'R':
                    continue
                if i == 0 and dominoes[i + 1] == 'L':
                    tmp[i] = 'L'
                    c = True
                    continue
                elif i == 0:
                    continue
                if i == len(dominoes) - 1 and dominoes[i - 1] == 'R':
                    tmp[i] = 'R'
                    c = True
                    continue
                elif i == len(dominoes) - 1:
                    continue
                if dominoes[i - 1] == 'R' and dominoes[i + 1] == 'L':
                    continue
                if dominoes[i - 1] == 'R':
                    tmp[i] = 'R'
                    c = True
                    continue
                if dominoes[i + 1] == 'L':
                    tmp[i] = 'L'
                    c = True
                    continue
            dominoes = tmp

        return "".join(dominoes)


class Solution2:
    def pushDominoes(self, dominoes: str) -> str:
        temp = ''
        while dominoes != temp:
            temp = dominoes
            dominoes = dominoes.replace('R.L', 'xxx')       # <-- 1)
            dominoes = dominoes.replace('R.', 'RR')         # <-- 2)
            dominoes = dominoes.replace('.L', 'LL')         # <-- 2)

        return dominoes.replace('xxx', 'R.L')
