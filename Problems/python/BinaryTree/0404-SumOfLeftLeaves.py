"""
Given the root of a binary tree, return the sum of all left leaves.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.

Example 2:

Input: root = [1]
Output: 0


Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """ DFS """
        ans = self.helper(root, 0, False)

        return ans

    def helper(self, node, ans, left):
        if not node:
            return 0

        if not node.left and not node.right and left is True:
            return node.val
        left_val = self.helper(node.left, ans, True)
        right_val = self.helper(node.right, ans, False)

        return left_val + right_val


class Solution2:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        """ BFS """
        stack = [[root, False]]
        ans = 0
        while stack:
            cur = stack.pop(0)
            node, left = cur[0], cur[1]
            if not node.left and not node.right:
                if left is True:
                    ans += node.val
            elif node.left and node.right:
                stack.append([node.left, True])
                stack.append([node.right, False])
            elif node.left:
                stack.append([node.left, True])
            elif node.right:
                stack.append([node.right, False])

        return ans
