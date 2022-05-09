"""
Given the roots of two binary trees root and subRoot, return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.

A subtree of a binary tree tree is a tree that consists of a node in tree and all of this node's descendants. The tree tree could also be considered as a subtree of itself.



Example 1:


Input: root = [3,4,5,1,2], subRoot = [4,1,2]
Output: true
Example 2:


Input: root = [3,4,5,1,2,null,null,null,null,0], subRoot = [4,1,2]
Output: false


Constraints:

The number of nodes in the root tree is in the range [1, 2000].
The number of nodes in the subRoot tree is in the range [1, 1000].
-10^4 <= root.val <= 10^4
-10^4 <= subRoot.val <= 10^4
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """ BFS """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop(0)
            if self.same(node, subRoot):
                return True
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return False

    def dfs(self, node, sub):
        if not node:
            return False
        if self.same(node, sub):
            return True

        return self.dfs(node.left, sub) or self.dfs(node.right, sub)

    def same(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        if node1.val == node2.val:
            return self.same(node1.left, node2.left) and self.same(node1.right, node2.right)


class Solution2:
    """ DFS """
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        return self.dfs(root, subRoot)

    def dfs(self, node, sub):
        if not node:
            return False
        if self.same(node, sub):
            return True

        return self.dfs(node.left, sub) or self.dfs(node.right, sub)

    def same(self, node1, node2):
        if not node1 and not node2:
            return True
        elif not node1 or not node2:
            return False
        if node1.val == node2.val:
            return self.same(node1.left, node2.left) and self.same(node1.right, node2.right)
