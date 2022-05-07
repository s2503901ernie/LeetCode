"""
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.



Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.


Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """ DFS: Use strings to do the comparison. """
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        node_list = []
        while head:
            node_list.append(str(head.val))
            head = head.next
        path = "".join(node_list)
        return self.helper(path, "", root)

    def helper(self, path, cur, node):
        if not node:
            return False
        new_cur = cur + str(node.val)
        if path in new_cur:
            return True
        return self.helper(path, new_cur, node.left) or self.helper(path, new_cur, node.right)


class Solution2:
    """ Double DFS: If root node is not true, go for left and right child. """
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.dfs(head, root) is True:
            return True
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def dfs(self, head, root):
        if not head:
            return True
        if not root:
            return False
        if head.val == root.val:
            return self.dfs(head.next, root.left) or self.dfs(head.next, root.right)
