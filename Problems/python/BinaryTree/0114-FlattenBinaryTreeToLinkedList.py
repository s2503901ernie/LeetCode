"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.


Example 1:


Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


Follow up: Can you flatten the tree in-place (with O(1) extra space)?
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        self.dfs(root)

        return root

    def dfs(self, node):
        if not node:
            return
        if node.left and not node.right:
            node.right = node.left
        elif node.left and node.right:
            node.right = self.connect(node.left, node.right)
        node.left = None
        if node.right:
            self.dfs(node.right)

    def connect(self, left, right):
        if not left:
            return right
        if not right:
            return left
        if not left.right:
            left.right = right
            return left
        else:
            cur = left.right
            while cur:
                if cur.right:
                    cur = cur.right
                else:
                    break
            cur.right = right
            return left


class Solution2:
    """Time: O(n), Space: O(n)"""
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        ans = []
        self.dfs(root, ans)
        for i in range(len(ans) - 1):
            ans[i].left = None
            ans[i].right = ans[i + 1]

    def dfs(self, node, ans):
        if not node:
            return
        ans.append(node)
        self.dfs(node.left, ans)
        self.dfs(node.right, ans)
