"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


Constraints:

The number of nodes in the tree is in the range [0, 10^5].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        return self.get_depth(root, depth=1)

    def get_depth(self, node, depth):
        if not node.left and not node.right:
            return depth
        elif node.left and not node.right:
            return self.get_depth(node.left, depth + 1)
        elif node.right and not node.left:
            return self.get_depth(node.right, depth + 1)
        else:
            left_depth = self.get_depth(node.left, depth + 1)
            right_depth = self.get_depth(node.right, depth + 1)
            return min(left_depth, right_depth)


class Solution2:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        ans = []
        self.get_depth(root, 0, ans)

        return min(ans) + 1

    def get_depth(self, node, depth, ans):
        if node is None:
            return
        if node.left is None and node.right is None:
            ans.append(depth)
        self.get_depth(node.left, depth+1, ans)
        self.get_depth(node.right, depth+1, ans)
