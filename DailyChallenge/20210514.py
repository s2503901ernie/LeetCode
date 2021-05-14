"""
Given the root of a binary tree, flatten the tree into a "linked list":

The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Input: root = []
Output: []

Input: root = [0]
Output: [0]

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
 

Follow up: Can you flatten the tree in-place (with O(1) extra space)?

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return []
        self.pre_order(root)

        
    def pre_order(self, root):
        if root.left is not None:
            sub_left = root.left
            sub_right = root.right
            root.right = self.connect(sub_left, sub_right)
            root.left = None
        if root.right is not None:
            self.pre_order(root.right)
            
    def connect(self, left_subtree, right_subtree):
        if left_subtree.right is None:
            left_subtree.right = right_subtree
            return left_subtree
        current = left_subtree.right
        while current.right is not None:
            current = current.right
        current.right = right_subtree
        return left_subtree
