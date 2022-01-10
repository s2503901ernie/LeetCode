"""
Given a string s which represents an expression, evaluate this expression and return its value.

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().



Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5


Constraints:

1 <= s.length <= 3 * 10^5
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 2^31 - 1].
The answer is guaranteed to fit in a 32-bit integer.
"""
class Solution:
    def calculate(self, s: str) -> int:
        s += "d"
        stack = []
        current = ""
        pre_flag = "+"

        for c in s:
            if c == " ":
                continue
            if c.isdigit() is True:
                current = current + c
            else:
                if pre_flag == "+":
                    stack.append(int(current))
                elif pre_flag == "-":
                    stack.append(-int(current))
                elif pre_flag == "*":
                    stack.append(stack.pop() * int(current))
                else:
                    stack.append(int(stack.pop() / int(current)))
                current = ""
                pre_flag = c

        return sum(stack)
