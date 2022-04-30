"""
Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.



Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 3

Example 2:
Input: root = [1,null,2]
Output: 2

Example 3:
Input: root = []
Output: 0

Example 4:
Input: root = [0]
Output: 1

Constraints:

The number of nodes in the tree is in the range [0, 104].
-100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    """ DFS """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        depths = []
        self.get_depth(root, 0, depths)
        if not depths:
            return 0

        return max(depths)

    def get_depth(self, node, depth, array):
        if node is None:
            return
        depth += 1
        if node.left is None and node.right is None:
            array.append(depth)
        self.get_depth(node.left, depth, array)
        self.get_depth(node.right, depth, array)


class Solution2:
    """ DFS """
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_depth(root, 0)

    def get_depth(self, node, depth):
        if not node:
            return depth
        depth += 1
        left_depth = self.get_depth(node.left, depth)
        right_depth = self.get_depth(node.right, depth)
        return max(left_depth, right_depth, depth)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """ BFS """
        if not root:
            return 0
        depth = 0
        stack = [root]
        while stack:
            for i in range(len(stack)):
                cur = stack.pop(0)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            depth += 1

        return depth
