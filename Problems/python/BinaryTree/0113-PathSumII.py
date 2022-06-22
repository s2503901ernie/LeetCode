"""
Given the root of a binary tree and an integer targetSum, return all root-to-leaf paths where the sum of the node values in the path equals targetSum. Each path should be returned as a list of the node values, not node references.

A root-to-leaf path is a path starting from the root and ending at any leaf node. A leaf is a node with no children.



Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: [[5,4,11,2],[5,8,4,5]]
Explanation: There are two paths whose sum equals targetSum:
5 + 4 + 11 + 2 = 22
5 + 8 + 4 + 5 = 22

Example 2:


Input: root = [1,2,3], targetSum = 5
Output: []

Example 3:

Input: root = [1,2], targetSum = 0
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """dfs"""
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        self.dfs(root, 0, [], targetSum, ans)

        return ans

    def dfs(self, node, cur, nodes, t, ans):
        new = nodes + [node.val]
        cur += node.val
        if node.left:
            self.dfs(node.left, cur, new, t, ans)
        if node.right:
            self.dfs(node.right, cur, new, t, ans)
        if not node.left and not node.right:
            if cur == t:
                ans.append(new)


class Solution2:
    """bfs"""
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        ans = []
        stack = [[root, 0, []]]
        while stack:
            cur = stack.pop(0)
            node, cur_sum, nodes = cur[0], cur[1], cur[2]
            cur_sum += node.val
            new = nodes + [node.val]
            if node.left:
                stack.append([node.left, cur_sum, new])
            if node.right:
                stack.append([node.right, cur_sum, new])
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    ans.append(new)

        return ans

        