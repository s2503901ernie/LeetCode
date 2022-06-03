"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).



Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true

Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-100 <= Node.val <= 100
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """DFS"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        return self.judge(root.left, root.right)

    def judge(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False
        if left.val == right.val:
            out_pair = self.judge(left.left, right.right)
            in_pair = self.judge(left.right, right.left)

            return in_pair and out_pair


class Solution2:
    """BFS"""
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        stack = [root]
        while stack:
            tmp = []
            for _ in range(len(stack)):
                node = stack.pop(0)
                if node:
                    stack.append(node.left)
                    stack.append(node.right)
                    tmp.append(node.val)
                else:
                    tmp.append(None)

            left = 0
            right = len(tmp) - 1
            while left < right:
                if tmp[left] == tmp[right]:
                    left += 1
                    right -= 1
                else:
                    return False

        return True
