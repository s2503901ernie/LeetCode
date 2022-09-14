"""
Given a binary tree where node values are digits from 1 to 9. A path in the binary tree is said to be pseudo-palindromic if at least one permutation of the node values in the path is a palindrome.

Return the number of pseudo-palindromic paths going from the root node to leaf nodes.



Example 1:



Input: root = [2,3,1,3,1,null,1]
Output: 2
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the red path [2,3,3], the green path [2,1,1], and the path [2,3,1]. Among these paths only red path and green path are pseudo-palindromic paths since the red path [2,3,3] can be rearranged in [3,2,3] (palindrome) and the green path [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 2:



Input: root = [2,1,1,1,3,null,null,null,null,null,1]
Output: 1
Explanation: The figure above represents the given binary tree. There are three paths going from the root node to leaf nodes: the green path [2,1,1], the path [2,1,3,1], and the path [2,1]. Among these paths only the green path is pseudo-palindromic since [2,1,1] can be rearranged in [1,2,1] (palindrome).
Example 3:

Input: root = [9]
Output: 1


Constraints:

The number of nodes in the tree is in the range [1, 10^5].
1 <= Node.val <= 9
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """bit manipulation."""
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, 0)

        return self.ans

    def dfs(self, node, cur):
        if not node:
            return
        cur ^= 1 << (node.val - 1)
        if not node.left and not node.right:
            if cur & (cur - 1) == 0:
                self.ans += 1
            return
        self.dfs(node.left, cur)
        self.dfs(node.right, cur)


class Solution2:
    """set."""
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.dfs(root, set())

        return self.ans

    def dfs(self, node, cur):
        if not node:
            return
        new = cur.copy()
        if node.val in new:
            new.remove(node.val)
        else:
            new.add(node.val)
        if not node.left and not node.right:
            if len(new) == 0 or len(new) == 1:
                self.ans += 1
            return
        self.dfs(node.left, new)
        self.dfs(node.right, new)
