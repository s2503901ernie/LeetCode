"""
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.



Example 1:


Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:

Input: root = [1,null,3]
Output: [1,3]

Example 3:

Input: root = []
Output: []


Constraints:

The number of nodes in the tree is in the range [0, 100].
-100 <= Node.val <= 100
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        max_depth = self.find_maxdepth(root, 0)
        order = []
        ans = []
        self.helper(root, 0, order)
        n = 0
        while n <= max_depth:
            for node in order:
                if node[0] == n:
                    ans.append(node[1])
                    n += 1
        return ans

    def helper(self, node, depth, ans):
        if node is not None:
            ans.append([depth, node.val])
            self.helper(node.right, depth + 1, ans)
            self.helper(node.left, depth + 1, ans)

    def find_maxdepth(self, node, depth):
        if node is None:
            return 0
        left_max_depth = self.find_maxdepth(node.left, depth + 1)
        right_max_depth = self.find_maxdepth(node.right, depth + 1)
        return max(left_max_depth, right_max_depth, depth)

    def rightSideView2(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        level = []
        ans = []
        self.get_level_order(root, 0, level)
        for array in level:
            ans.append(array[-1])

    def get_level_order(self, node, depth, array):
        if not node:
            return
        if len(array) < depth + 1:
            array.append([node.val])
        else:
            array[depth].append(node.val)
        self.get_level_order(node.left, depth+1, array)
        self.get_level_order(node.right, depth+1, array)


class Solution2:
    """bfs"""
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stack = [root]
        nodes = []
        while stack:
            tmp = []
            for _ in range(len(stack)):
                cur = stack.pop(0)
                tmp.append(cur.val)
                if cur.left:
                    stack.append(cur.left)
                if cur.right:
                    stack.append(cur.right)
            nodes.append(tmp)
        ans = []
        for n in nodes:
            ans.append(n[-1])

        return ans


class Solution3:
    """dfs"""
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        nodes = []
        ans = []
        self.dfs(root, 0, nodes)
        for n in nodes:
            ans.append(n[-1])

        return ans

    def dfs(self, node, depth, ans):
        if not node:
            return
        if len(ans) < depth + 1:
            ans.append([node.val])
        else:
            ans[depth].append(node.val)
        self.dfs(node.left, depth + 1, ans)
        self.dfs(node.right, depth + 1, ans)
