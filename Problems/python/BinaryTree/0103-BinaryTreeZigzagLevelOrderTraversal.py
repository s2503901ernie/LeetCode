"""
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).



Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
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
        elif depth % 2 == 1:
            ans[depth].insert(0, node.val)
        else:
            ans[depth].append(node.val)
        self.helper(node.left, depth+1, ans)
        self.helper(node.right, depth+1, ans)
