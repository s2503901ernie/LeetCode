"""
Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, and every node has no left child and only one right child.



Example 1:


Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9]

Example 2:


Input: root = [5,1,7]
Output: [1,null,5,null,7]


Constraints:

The number of nodes in the given tree will be in the range [1, 100].
0 <= Node.val <= 1000
"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        res = []
        self.helper(root, res)
        if len(res) == 1:
            return TreeNode(res[0])
        root = TreeNode(res[0])
        node = root
        for val in res[1:]:
            node.right = TreeNode(val)
            node = node.right

        return root

    def helper(self, node, res):
        if node:
            self.helper(node.left, res)
            res.append(node.val)
            self.helper(node.right, res)


class Solution2:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        return self.helper(root, None)

    def helper(self, node, parent):
        if not node:
            return parent
        left = self.helper(node.left, node)
        node.left = None
        node.right = self.helper(node.right, parent)

        return left


class Solution3:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        node = root
        parent = TreeNode(0)
        dummy = parent
        stack = []
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            parent.right = node
            parent = parent.right
            node = node.right
            parent.left = None

        return dummy.right

