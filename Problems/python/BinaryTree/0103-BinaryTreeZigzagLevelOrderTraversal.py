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
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """DFS"""
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        ans = [[]]
        self.dfs(root, 0, ans)

        return ans

    def dfs(self, node, depth, ans):
        if not node:
            return
        if len(ans) < depth + 1:
            ans.append([node.val])
        elif depth % 2 == 1:
            ans[depth].insert(0, node.val)
        else:
            ans[depth].append(node.val)
        self.dfs(node.left, depth+1, ans)
        self.dfs(node.right, depth+1, ans)


class Solution2:
    """BFS"""
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        stack = [root]
        ans = []
        n = 0
        while stack:
            tmp = []
            if n == 1:
                for _ in range(len(stack)):
                    cur = stack.pop()
                    tmp.append(cur.val)
                    if cur.right:
                        stack.insert(0, cur.right)
                    if cur.left:
                        stack.insert(0, cur.left)
                ans.append(tmp)
                n = 0
            else:
                for _ in range(len(stack)):
                    cur = stack.pop(0)
                    tmp.append(cur.val)
                    if cur.left:
                        stack.append(cur.left)
                    if cur.right:
                        stack.append(cur.right)
                ans.append(tmp)
                n = 1

        return ans

