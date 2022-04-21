"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[]]
        self.helper(root, 0, ans)

        return ans

    def helper(self, node, depth, ans):
        if not node:
            return
        if len(ans) < depth + 1:
            ans.append([node.val])
        else:
            ans[depth].append(node.val)
        self.helper(node.left, depth+1, ans)
        self.helper(node.right, depth+1, ans)
